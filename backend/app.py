from __future__ import annotations

import argparse
import json
import logging
import os
import queue
import threading
import time
from pathlib import Path
from typing import List, Set

from dotenv import load_dotenv

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import movelladot_pc_sdk as sdk
from xdpchandler import XdpcHandler

from classify import run_classifier

_classifier_stop_event = threading.Event()

load_dotenv()

INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = os.getenv("INFLUX_ORG")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")
INFLUX_URL = os.getenv("INFLUX_URL")

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
influx_writer = influx_client.write_api(write_options=SYNCHRONOUS)

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("dot-backend")

try:
    from flask import Flask, Response, request
    from flask_cors import CORS
except ImportError:
    Flask = None  # type: ignore

app = Flask(__name__) if Flask else None
if app:
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

_hdl_lock = threading.Lock()
_stream_threads: dict[str, threading.Thread] = {}
_stream_stop_flags: dict[str, threading.Event] = {}
_evt_clients: Set[queue.Queue[str]] = set()

MIN_ACTIVE_DOTS = 2
GRACE_PERIOD_SECS = 3.0

_connected_handler: XdpcHandler | None = None
_connected_dots: list[sdk.XsDotDevice] = []

_timeout_timers: list[threading.Timer] = []


def _is_dot_session_alive(hd: XdpcHandler, dots: list[sdk.XsDotDevice]) -> bool:
    if not hd or not dots:
        return False

    for d in dots:
        try:
            _ = d.batteryLevel()
            return True
        except Exception:
            pass

    try:
        _ = hd.manager()
        return True
    except Exception:
        return False


def _disconnect_all():
    global _connected_handler, _connected_dots
    hd = _connected_handler
    dots = list(_connected_dots)

    _connected_handler = None
    _connected_dots = []

    for d in dots:
        try:
            d.stopMeasurement()
        except Exception:
            pass

    if hd:
        try:
            hd.cleanup()
        except Exception:
            pass


def connect_all_dots(force: bool = False) -> tuple[XdpcHandler, list[sdk.XsDotDevice]]:
    global _connected_handler, _connected_dots

    if not force and _connected_handler and _connected_dots:
        if _is_dot_session_alive(_connected_handler, _connected_dots):
            log.info("Reusing existing DOT connection.")
            return _connected_handler, _connected_dots
        log.warning("Existing DOT connection is stale; reconnecting.")
        _disconnect_all()

    if _connected_handler:
        _disconnect_all()

    time.sleep(0.5)

    hd = XdpcHandler()
    if not hd.initialize():
        raise RuntimeError("Init failed – Bluetooth adapter up?")

    time.sleep(0.5)

    hd.scanForDots()
    if not hd.detectedDots():
        hd.cleanup()
        raise RuntimeError("No DOT advertisements found.")

    hd.connectDots()
    connected = hd.connectedDots()
    time.sleep(1)

    if not connected:
        hd.cleanup()
        raise RuntimeError("Could not connect to any DOT.")

    _connected_handler = hd
    _connected_dots = connected
    return hd, connected


def _stream_worker(sensor_infos: list[tuple[str, str]], activity, stop_event: threading.Event) -> None:
    global _connected_handler, _connected_dots
    if not _connected_handler or not _connected_dots:
        raise RuntimeError("No connected DOTs – call /connect first.")

    hd = _connected_handler
    print(f"[worker] starting with {len(sensor_infos)} sensor(s)")

    dots: dict[str, tuple[sdk.XsDotDevice, str]] = {}
    for sid, body_part in sensor_infos:
        dot = next((d for d in _connected_dots if d.bluetoothAddress() == sid), None)
        if not dot:
            print(f"[worker] WARNING - {sid} not in connected dots list")
            continue
        addr = dot.bluetoothAddress()
        dots[addr] = (dot, body_part)
        print(f"[worker] {addr} mapped to body_part='{body_part}'")

    for addr, (dot, _) in dots.items():
        print(f"[worker] {addr} set profile → General")
        dot.setOnboardFilterProfile("General")

        try:
            payload = sdk.XsPayloadMode_RateQuantitieswMag
        except AttributeError:
            payload = sdk.XsPayloadMode_RateQuantities

        if dot.startMeasurement(payload):
            print(f"[worker] {addr} measurement started")
        else:
            print(f"[worker] ERROR - startMeasurement failed for {addr}: {dot.lastResultText()}")

    last_emit = time.time()
    print("[worker] entering packet loop")

    while not stop_event.is_set():
        idle = True
        for addr, (dot, body_part) in dots.items():
            pkt = None
            with _hdl_lock:
                if hd.packetAvailable(addr):
                    pkt = hd.getNextPacket(addr)

            if not pkt or not pkt.containsCalibratedAcceleration():
                continue

            idle = False
            ax, ay, az = pkt.calibratedAcceleration()

            try:
                ts = pkt.sampleTimeFine()
            except AttributeError:
                ts = (pkt.timeStampFine() if hasattr(pkt, "timeStampFine") else pkt.sampleTime() * 10_000)

            _broadcast(
                json.dumps({"id": addr, "ts": ts, "ax": ax, "ay": ay, "az": az}, separators=(",", ":"))
            )
            last_emit = time.time()

            influx_writer.write(
                bucket=INFLUX_BUCKET,
                org=INFLUX_ORG,
                record=(
                    Point("sensor_data")
                    .tag("sensor_id", addr)
                    .tag("body_part", body_part)
                    .tag("activity", activity)
                    .field("Acc_X", ax)
                    .field("Acc_Y", ay)
                    .field("Acc_Z", az)
                ),
            )
            time.sleep(0.003)

        if idle:
            if time.time() - last_emit > 1.0:
                _broadcast("{}")
                last_emit = time.time()
                print("[worker] heartbeat broadcast")
            time.sleep(0.003)

    print("[worker] stop_event set – stopping measurements")
    for addr, (dot, _) in dots.items():
        try:
            if dot.stopMeasurement():
                print(f"[worker] {addr} measurement stopped")
        except Exception as e:
            print(f"[worker] {addr} stopMeasurement error: {e}")

    print("[worker] exited cleanly")


def _stream_worker2(sensor_infos: list[tuple[str, str]], activity: str, stop_event: threading.Event) -> None:
    global _connected_handler, _connected_dots
    if not _connected_handler or not _connected_dots:
        raise RuntimeError("No connected DOTs – call /connect first.")

    hd = _connected_handler
    print(f"[worker] starting with {len(sensor_infos)} sensor(s)")

    dots: dict[str, tuple[sdk.XsDotDevice, str]] = {}
    for sid, body_part in sensor_infos:
        dot = next((d for d in _connected_dots if d.bluetoothAddress() == sid), None)
        if not dot:
            print(f"[worker] WARNING – {sid} not in connected list")
            continue
        dots[dot.bluetoothAddress()] = (dot, body_part)
        print(f"[worker] {sid} mapped to '{body_part}'")

    payload_full = sdk.XsPayloadMode_RateQuantitieswMag
    payload_light = sdk.XsPayloadMode_RateQuantities

    for addr, (dot, _) in dots.items():
        dot.setOnboardFilterProfile("General")
        if not dot.startMeasurement(payload_full):
            print(f"[worker] ERROR startMeasurement {addr}: {dot.lastResultText()}")

    last_good = {addr: time.time() for addr in dots}
    restart_tries = {addr: 0 for addr in dots}
    SILENCE_LIMIT = 2.0
    MAX_RESTARTS = 3

    while not stop_event.is_set():
        idle_loop = True

        for addr, (dot, body_part) in dots.items():
            pkt_processed = False

            with _hdl_lock:
                while hd.packetAvailable(addr):
                    pkt = hd.getNextPacket(addr)
                    if not pkt:
                        continue

                    if pkt.containsCalibratedAcceleration():
                        last_good[addr] = time.time()
                        restart_tries[addr] = 0
                        pkt_processed = True

                        ax, ay, az = pkt.calibratedAcceleration()
                        ts = getattr(pkt, "sampleTimeFine", lambda: 0)()

                        _broadcast(
                            json.dumps({"id": addr, "ts": ts, "ax": ax, "ay": ay, "az": az}, separators=(",", ":"))
                        )

                        influx_writer.write(
                            bucket=INFLUX_BUCKET,
                            org=INFLUX_ORG,
                            record=(
                                Point("sensor_data")
                                .tag("sensor_id", addr)
                                .tag("body_part", body_part)
                                .tag("activity", activity)
                                .field("Acc_X", ax)
                                .field("Acc_Y", ay)
                                .field("Acc_Z", az)
                            ),
                        )

            if time.time() - last_good[addr] > SILENCE_LIMIT:
                print(f"[worker] {addr} silent >{SILENCE_LIMIT}s – restarting")
                dot.stopMeasurement()
                time.sleep(0.1)

                use_payload = payload_light if restart_tries[addr] >= MAX_RESTARTS else payload_full

                if dot.startMeasurement(use_payload):
                    print(
                        f"[worker] {addr} measurement RE-started "
                        f"({'light' if use_payload==payload_light else 'full'})"
                    )
                    last_good[addr] = time.time()
                else:
                    print(f"[worker] {addr} restart failed: {dot.lastResultText()}")
                    restart_tries[addr] += 1

            idle_loop &= not pkt_processed

        time.sleep(0.003 if idle_loop else 0.0005)

    print("[worker] stop_event set – stopping measurements")
    for addr, (dot, _) in dots.items():
        dot.stopMeasurement()

    print("[worker] exited cleanly")


def _spawn_worker_with_timeout(target, args: tuple, timeout_s: int = 30):
    stop_evt = threading.Event()
    th = threading.Thread(target=target, args=(*args, stop_evt), daemon=True)
    th.start()

    timer = threading.Timer(timeout_s, stop_evt.set)
    _timeout_timers.append(timer)
    timer.start()

    return th


def _broadcast(msg: str) -> None:
    dead: List[queue.Queue[str]] = []
    for q in _evt_clients:
        try:
            q.put_nowait(msg)
        except Exception:
            dead.append(q)
    for q in dead:
        _evt_clients.discard(q)


def cli_scan() -> None:
    hd = XdpcHandler()
    if not hd.initialize():
        log.error("Init failed.")
        return
    hd.scanForDots()
    for p in hd.detectedDots():
        print("📡", p.bluetoothAddress())
    hd.cleanup()


def cli_stream(seconds: float) -> None:
    try:
        hd, dot = connect_all_dots()
    except RuntimeError as err:
        log.error("%s", err)
        return

    addr = dot.bluetoothAddress()
    dot.setOnboardFilterProfile("General")
    try:
        payload = sdk.XsPayloadMode_RateQuantitieswMag
    except AttributeError:
        payload = sdk.XsPayloadMode_RateQuantities

    if not dot.startMeasurement(payload):
        log.error("startMeasurement failed: %s", dot.lastResultText())
        hd.cleanup()
        return

    t0 = time.time()
    try:
        while time.time() - t0 < seconds:
            pkt = None
            with _hdl_lock:
                if hd.packetAvailable(addr):
                    pkt = hd.getNextPacket(addr)
            if pkt and pkt.containsOrientation():
                eul = pkt.orientationEuler()
                print(
                    f"{time.time()-t0:6.2f}s roll={eul.x():6.2f} pitch={eul.y():6.2f} yaw={eul.z():6.2f}"
                )
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        dot.stopMeasurement()
        hd.cleanup()


def _list_models(activity: str | None = None) -> list[str]:
    if not activity:
        return []
    base = MODEL_DIR / activity
    if not base.exists() or not base.is_dir():
        return []
    return sorted([p.name for p in base.iterdir() if p.suffix in {".pkl", ".joblib"}])


if app:

    @app.post("/connect")
    def api_connect():
        try:
            force = request.args.get("force") == "1"
            rescan = request.args.get("rescan") == "1"
            _, dots = connect_all_dots(force=force or rescan)
            return {"devices": [{"address": d.bluetoothAddress(), "id": d.deviceId().toXsString()} for d in dots]}
        except Exception as exc:
            log.error("Connection failed: %s", exc)
            return {"devices": [], "error": str(exc)}, 500

    @app.get("/devices")
    def api_devices():
        return {"devices": [{"address": d.bluetoothAddress(), "id": d.deviceId().toXsString()} for d in _connected_dots]}

    @app.post("/start")
    def api_start():
        sensor_id = request.args.get("sensor_id")
        body_part = request.args.get("body_part", "unassigned")
        activity = request.args.get("activity", "")
        duration = int(request.args.get("duration", -1))
        force = request.args.get("force") == "1"

        if not sensor_id:
            return {"error": "Missing sensor_id"}, 400

        try:
            connect_all_dots(force=False)
        except Exception:
            connect_all_dots(force=True)

        th = _stream_threads.get(sensor_id)

        if th and th.is_alive():
            if not force:
                return {"status": "already-running"}

            evt = _stream_stop_flags.get(sensor_id)
            if evt:
                evt.set()
            th.join(timeout=2.0)
            _stream_threads.pop(sensor_id, None)
            _stream_stop_flags.pop(sensor_id, None)

        stop_evt = threading.Event()
        _stream_stop_flags[sensor_id] = stop_evt
        th = threading.Thread(
            target=_stream_worker2,
            args=([(sensor_id, body_part)], activity, stop_evt),
            daemon=True,
        )
        _stream_threads[sensor_id] = th
        th.start()

        if duration > 0:
            threading.Timer(duration, stop_evt.set).start()

        return {"status": "started"}

    @app.post("/start-multiple")
    def api_start_multiple():
        data = request.get_json(force=True)

        sensors = [
            (s["sensor_id"], s["body_part"])
            for s in data.get("sensors", [])
            if s.get("sensor_id") and s.get("body_part")
        ]
        activity = (data.get("activity") or "").strip()
        model_name = (data.get("model_name") or "").strip()

        try:
            duration = int(data.get("duration", 30))
        except (TypeError, ValueError):
            return {"error": "duration must be an integer"}, 400

        if not sensors:
            return {"error": "No valid sensors provided"}, 400

        try:
            connect_all_dots(force=False)
        except Exception:
            connect_all_dots(force=True)

        if model_name and "/" not in model_name and activity:
            model_name = f"{activity}/{model_name}"

        try:
            if model_name:
                candidate = MODEL_DIR / model_name
                if not candidate.exists():
                    return {"error": f"Model not found: {candidate.name} for activity '{activity}'"}, 404
        except Exception:
            pass

        th = _spawn_worker_with_timeout(_stream_worker, (sensors, activity), duration)

        _classifier_stop_event.clear()
        threading.Thread(
            target=run_classifier,
            args=(activity, duration, _classifier_stop_event, model_name),
            daemon=True,
        ).start()

        return {"status": "started", "count": len(sensors), "duration": duration}

    @app.get("/models")
    def api_models():
        try:
            activity = request.args.get("activity", "").strip()
            models = _list_models(activity) if activity else []
            return {"activity": activity, "models": models}
        except Exception as e:
            log.error("Failed to list models: %s", e)
            return {"error": str(e)}, 500

    @app.get("/battery")
    def api_battery():
        sensor_id = request.args.get("sensor_id")
        if not sensor_id:
            return {"error": "Missing sensor_id"}, 400
        dot = next((d for d in _connected_dots if d.bluetoothAddress() == sensor_id), None)
        if not dot:
            return {"error": f"DOT {sensor_id} not connected"}, 404
        return {"battery": {"level": dot.batteryLevel(), "charging": dot.isCharging()}, "hertz": dot.outputRate()}

    @app.post("/stop")
    def api_stop():
        sensor_id = request.args.get("sensor_id")
        if not sensor_id:
            return {"error": "Missing sensor_id"}, 400
        evt = _stream_stop_flags.get(sensor_id)
        if evt:
            evt.set()
            return {"status": f"stopping {sensor_id}"}
        return {"status": f"not running {sensor_id}"}

    @app.post("/stop-all")
    def api_stop_all():
        for timer in _timeout_timers:
            timer.cancel()
        _timeout_timers.clear()

        for sensor_id, evt in list(_stream_stop_flags.items()):
            evt.set()
        _stream_stop_flags.clear()
        _stream_threads.clear()
        _classifier_stop_event.set()
        return {"status": "all stopped"}

    @app.get("/events")
    def api_events():
        q: queue.Queue[str] = queue.Queue(maxsize=2048)
        _evt_clients.add(q)

        def gen():
            try:
                while True:
                    yield f"data:{q.get()}\n\n"
            finally:
                _evt_clients.discard(q)

        return Response(gen(), mimetype="text/event-stream", headers={"Cache-Control": "no-cache"})

    @app.get("/stream")
    def api_stream_alias():
        return api_events()

    @app.post("/sync")
    def api_sync():
        if not _connected_handler or not _connected_dots:
            return {"error": "No connected DOTs — call /connect first."}, 400

        mgr = _connected_handler.manager()
        devices = _connected_dots
        root_mac = devices[-1].bluetoothAddress()

        try:
            if mgr.startSync(root_mac):
                log.info("Sync started; root node → %s", root_mac)
                return {"status": "syncing"}

            if mgr.lastResult() == sdk.XRV_SYNC_COULD_NOT_START:
                log.warning("Devices already in sync mode — resetting first")
                mgr.stopSync()
                time.sleep(0.1)
                if mgr.startSync(root_mac):
                    log.info("Sync restarted successfully")
                    return {"status": "syncing"}

            raise RuntimeError(mgr.lastResultText())

        except Exception as exc:
            log.error("Sync failed: %s", exc)
            return {"error": str(exc)}, 500

    @app.get("/classification")
    def api_classification():
        try:
            query = f"""
            from(bucket: "{INFLUX_BUCKET}")
            |> range(start: -3s)
            |> filter(fn: (r) => r._measurement == "classification")
            |> filter(fn: (r) => r._field == "action")
            |> last()
            """

            query_api = influx_client.query_api()
            result = query_api.query(org=INFLUX_ORG, query=query)

            if not result or not result[0].records:
                return {"time": None, "action": None}

            record = result[0].records[0]
            return {"time": record.get_time().isoformat(), "action": record.get_value()}

        except Exception as e:
            log.error("Failed to query classification: %s", e)
            return {"error": str(e)}, 500

    @app.get("/classification/summary")
    def api_classification_summary():
        try:
            start = request.args.get("start")
            end = request.args.get("end")

            if start and end:
                range_clause = f'range(start: time(v: "{start}"), stop: time(v: "{end}"))'
            else:
                secs = int(request.args.get("seconds", 120))
                if secs <= 0:
                    return {"error": "seconds must be >0"}, 400
                range_clause = f"range(start: -{secs}s)"

            query = f"""
                from(bucket: "{INFLUX_BUCKET}")
                |> {range_clause}
                |> filter(fn: (r) => r._measurement == "classification" and
                                    r._field == "action")
                |> aggregateWindow(every: 1s, fn: last, createEmpty: false)
                |> map(fn: (r) => ({{
                    r with ones: 1
                }}))
                |> group(columns: ["_value"])
                |> sum(column: "ones")
                |> rename(columns: {{ _value: "action", ones: "count" }})
                |> keep(columns: ["action", "count"])
            """

            result = influx_client.query_api().query(org=INFLUX_ORG, query=query)
            return [
                {"action": int(rec.values["action"]), "count": int(rec.values["count"])}
                for table in result
                for rec in table.records
            ]

        except Exception as e:
            log.error("Failed to build summary: %s", e)
            return {"error": str(e)}, 500


def main() -> None:
    parser = argparse.ArgumentParser(description="Movella DOT backend (60 Hz)")
    parser.add_argument("--scan", action="store_true", help="scan & exit")
    parser.add_argument("--stream", action="store_true", help="CLI stream & exit")
    parser.add_argument("--seconds", type=float, default=10.0, help="duration for --stream")
    parser.add_argument("--serve", action="store_true", help="run Flask SSE server")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    print("🧪 Parsed args:", args)

    if args.scan:
        cli_scan()
        return
    if args.stream:
        cli_stream(args.seconds)
        return

    if not app:
        print("Flask not installed – falling back to --scan")
        cli_scan()
        return

    log.info("Running Flask server on %s:%d", args.host, args.port)
    app.run(host=args.host, port=args.port, threaded=True)


if __name__ == "__main__":
    main()
