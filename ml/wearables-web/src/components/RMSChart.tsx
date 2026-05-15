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
import "./styles/RMSChart.css";
import type { Sensor } from "../pages/ManageWearables";

const API = import.meta.env.VITE_BACKEND_URL ?? "http://localhost:5000";

interface RMSChartProps {
  sensor: Sensor;
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

export default function RMSChart({ sensor }: RMSChartProps) {
  const [data, setData] = useState<Point[]>([]);
  const [count, setCount] = useState(0);
  const esRef = useRef<EventSource | null>(null);
  const t0Ref = useRef<number | null>(null);

  useEffect(() => {
    const es = new EventSource(`${API}/events`);
    esRef.current = es;

    // reset when sensor changes
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
          return next.filter((p) => t - p.t <= 60);
        });
        setCount((c) => c + 1);
      } catch {

      }
    };

    es.onerror = () => console.warn("SSE error in RMSChart (will keep listening)");

    return () => {
      es.close();
    };
  }, [sensor.address]);


  return (
    <div className="rmschart-container">
      <div className="rmschart-header">
        <span className="tag">TAG ID {sensor.id}</span>
        <span className="address">{sensor.address}</span>
        <span className="samples">{count} pts</span>
      </div>

      <div className="rmschart-graph">
        <ResponsiveContainer>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" dataKey="t" unit="s" domain={["auto", "auto"]} />
            <YAxis dataKey="rms" unit=" m/s²" domain={[0, 30]} allowDataOverflow />
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
      </div>
    </div>
  );
}
