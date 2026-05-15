import { useEffect, useRef, useState } from "react";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import "./styles/ViewRMS.css";
import type { Sensor } from "../pages/ManageWearables";

// Override with VITE_BACKEND_URL in .env if needed
const API = import.meta.env.VITE_BACKEND_URL ?? "http://localhost:5000";

interface ViewRMSProps {
  sensor: Sensor;
  onClose: () => void;
}

interface Packet {
  ts: number;
  ax?: number;
  ay?: number;
  az?: number;
  id?: string;
}

interface Point {
  t: number;
  rms: number;
}

const MAX_POINTS = 600;

export default function ViewRMS({ sensor, onClose }: ViewRMSProps) {
  const [data, setData] = useState<Point[]>([]);
  const [count, setCount] = useState(0);
  const t0Ref = useRef<number | null>(null);
  const esRef = useRef<EventSource | null>(null);

  useEffect(() => {
    const es = new EventSource(`${API}/events`);
    esRef.current = es;

    setData([]);
    setCount(0);
    t0Ref.current = null;

    es.onmessage = (ev) => {
      try {
        const p: Packet = JSON.parse(ev.data);
        if (p.id !== sensor.address) return;               
        if (p.ax == null || p.ay == null || p.az == null) return;

        const rms = Math.sqrt(p.ax ** 2 + p.ay ** 2 + p.az ** 2);
        const tsSec = (p.ts ?? 0) / 1e4;                   
        if (t0Ref.current === null) t0Ref.current = tsSec; 
        const t = tsSec - t0Ref.current;

        setData((old) => {
          const next = [...old, { t, rms }];
          return next.length > MAX_POINTS ? next.slice(-MAX_POINTS) : next;
        });
        setCount((c) => c + 1);
      } catch {
      }
    };

    es.onerror = () => console.warn("SSE error in ViewRMS (still listening)");

    return () => es.close();
  }, [sensor.address]);

  useEffect(() => {

    fetch(
      `${API}/start?force=1` +                      
      `&sensor_id=${encodeURIComponent(sensor.address)}` +
      `&body_part=${encodeURIComponent(sensor.name ?? "unknown")}`,
      { method: "POST" }
    ).catch(console.error);

    return () => {
      fetch(
        `${API}/stop?sensor_id=${encodeURIComponent(sensor.address)}`,
        { method: "POST" }
      ).catch(console.error);
    };
  }, [sensor.address]);

  return (
    <div className="viewrms-overlay">
      <div className="viewrms-modal">
        <div className="viewrms-header">
          <span className="tag">TAG ID&nbsp;{sensor.id}</span>
          <span className="address">{sensor.address}</span>
        </div>
        <hr />

        {/* body – RMS chart */}
        <div className="viewrms-body">
          <div style={{ position: "relative", width: "100%", height: 320 }}>
            <ResponsiveContainer>
              <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" dataKey="t" unit="s" domain={["auto", "auto"]} />
                <YAxis dataKey="rms" unit=" m/s²" domain={[0, 100]} allowDataOverflow />
                <Tooltip
                  formatter={(v: number) => `${v.toFixed(2)} m/s²`}
                  labelFormatter={(l: number) => `${l.toFixed(1)} s`}
                />
                <Line
                  type="monotone"
                  dataKey="rms"
                  isAnimationActive={false}
                  strokeWidth={2}
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>

            <span
              style={{
                position: "absolute",
                right: 8,
                top: 8,
                fontSize: 12,
                background: "rgba(0,0,0,.6)",
                color: "white",
                padding: "2px 4px",
                borderRadius: 4,
              }}
            >
              {count}
            </span>
          </div>
        </div>

        <div className="viewrms-footer">
          <button className="close-btn" onClick={onClose}>
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
