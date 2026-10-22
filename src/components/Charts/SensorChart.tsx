// SensorChart.tsx  (React 18 + TypeScript)

import { useEffect, useRef, useState } from "react";
import { io, Socket } from "socket.io-client";
import { LineChart, Line, XAxis, YAxis } from "recharts";
import type { DefaultEventsMap } from "@socket.io/component-emitter";

/* ------------------------------------------------------------------ */
/* 1.  Types                                                           */
/* ------------------------------------------------------------------ */
interface DotPacket {
  t: number;        // timestamp (seconds since stream start)
  ax: number;       // X-axis acceleration
  // ay, az, action … add here if you need them later
}

// The Socket.IO instance type
type IOSocket = Socket<DefaultEventsMap, DefaultEventsMap>;

/* ------------------------------------------------------------------ */
/* 2.  React component                                                 */
/* ------------------------------------------------------------------ */
export default function SensorChart() {
  /* 2-a. socketRef now initialised to null — fixes the TS error */
  const socketRef = useRef<IOSocket | null>(null);

  /* 2-b. keep last ~5 seconds of data (300 points @60 Hz) */
  const [series, setSeries] = useState<DotPacket[]>([]);

  useEffect(() => {
    /* 3.  Open the WebSocket */
    socketRef.current = io("http://localhost:5000/stream");

    /* 4.  Handle incoming packets */
    socketRef.current.on("dot-data", (pkt: DotPacket) => {
      setSeries(prev => {
        const next = [...prev, pkt];
        return next.length > 300 ? next.slice(-300) : next;
      });
    });

    /* 5.  Clean up on unmount */
    return () => {
      socketRef.current?.disconnect();
      socketRef.current = null;
    };
  }, []); // ← empty deps → run once

  /* ---------------------------------------------------------------- */
  /* 6.  Render                                                       */
  /* ---------------------------------------------------------------- */
  return (
    <LineChart width={600} height={300} data={series}>
      {/* hide the X-axis because we’re using relative time */}
      <XAxis dataKey="t" hide />
      <YAxis domain={[-2, 2]} />
      <Line
        type="monotone"
        dataKey="ax"
        dot={false}
        isAnimationActive={false}   /* smoother live updates */
      />
    </LineChart>
  );
}
