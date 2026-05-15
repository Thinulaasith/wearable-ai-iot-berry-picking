import { useEffect, useState } from "react";
import { Spinner, Button } from "react-bootstrap";
import SensorCard from "../components/SensorCard";
import ViewRMS from "../components/ViewRMS";
import "../styles/ManageWearables.css";
import { useSensorContext } from "../context/SensorContext";
import type { LargeNumberLike } from "crypto";

export interface Sensor {
  address: string;   // DOT MAC
  id: string;
  name: string;
  batteryLevel: number;
  chargingStatus: boolean;
  hertzMode: number;
}

const API = import.meta.env.VITE_BACKEND_URL ?? "http://localhost:5000";

const fetchBattery = async (s: Sensor): Promise<Sensor> => {
  try {
    const r = await fetch(`${API}/battery?sensor_id=${s.address}`);
    if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
    const { battery: { level, charging }, hertz } = await r.json();
    return { ...s, batteryLevel: level, chargingStatus: charging, hertzMode: hertz };
  } catch {
    return s;
  }
};

export default function ManageWearablesPage() {
  const { sensors, setSensors, selected, setSelected } = useSensorContext();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [busyMsg, setBusyMsg] = useState<string>("");

  const connectAndFetch = async (opts?: { force?: boolean; rescan?: boolean }) => {
    setBusy(true);
    setBusyMsg(opts?.force ? "Reconnecting…" : opts?.rescan ? "Rescanning…" : "Connecting…");
    setError(null);
    try {
      const qs = new URLSearchParams();
      if (opts?.force) qs.set("force", "1");
      if (opts?.rescan) qs.set("rescan", "1");
      await fetch(`${API}/connect${qs.toString() ? `?${qs}` : ""}`, { method: "POST" });

      const res = await fetch(`${API}/devices`);
      const { devices = [] } = (await res.json()) as { devices: { address: string; id: string }[] };

      const base = devices.map(d => ({
        address: d.address,
        id: d.id,
        name: d.id || d.address,
        batteryLevel: -1,
        chargingStatus: false,
        hertzMode: -1
      }));

      const withBatt = await Promise.all(base.map(fetchBattery));
      setSensors(withBatt);
    } catch (err: any) {
      setError(err.message ?? String(err));
    } finally {
      setBusy(false);
    }
  };

  const syncSensors = async () => {
    setBusy(true);
    setBusyMsg("Syncing…");
    setError(null);
    try {
      const r = await fetch(`${API}/sync`, { method: "POST" });
      if (!r.ok) {
        const { error } = await r.json();
        throw new Error(error ?? `${r.status} ${r.statusText}`);
      }
    } catch (err: any) {
      setError(err.message ?? String(err));
    } finally {
      setBusy(false);
    }
  };

  /* ── poll battery every 10 s ── */
  useEffect(() => {
    if (!sensors.length) return;
    const id = setInterval(async () => {
      const updated = await Promise.all(sensors.map(fetchBattery));
      setSensors(updated);
    }, 10_000);
    return () => clearInterval(id);
  }, [sensors]);


  return (
    <div className="manage-devices-container">
      {busy ? (
        <div className="spinner-wrap">
          <Spinner animation="border" role="status" />
          <p className="spinner-text">{busyMsg}</p>
        </div>
      ) : (
        <>
          <h1 className="manage-devices-title">Manage Devices</h1>
          <hr className="manage-devices-divider" />

          <Button className="primary" onClick={() => connectAndFetch()} disabled={busy}>
            Connect Sensors
          </Button>

          <Button className="ms-2" variant="outline-primary" onClick={() => connectAndFetch({ rescan: true })} disabled={busy}>
            Rescan for Missed Sensors
          </Button>
          
          {error && <p style={{ color: "red" }}>{error}</p>}

          <div className="sensor-list">
            {sensors.map(s => (
              <SensorCard
                key={s.address}
                sensor={s}
                onViewRMS={() => setSelected(s)}
              />
            ))}
          </div>

          <Button
            variant="secondary"
            className="ms-2"
            onClick={syncSensors}
            disabled={busy || !sensors.length}
          >
            Sync Sensors
          </Button>

          {selected && (
            <ViewRMS sensor={selected} onClose={() => setSelected(null)} />
          )}
        </>
      )}
    </div>
  );
}
