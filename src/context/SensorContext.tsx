// src/context/SensorContext.tsx
import React, { createContext, useContext, useState } from 'react';
import type { ReactNode } from 'react';
import type { Sensor } from '../pages/ManageWearables';

interface SensorContextType {
  sensors: Sensor[];
  setSensors: React.Dispatch<React.SetStateAction<Sensor[]>>;
  selected: Sensor | null;
  setSelected: React.Dispatch<React.SetStateAction<Sensor | null>>;
}

const SensorContext = createContext<SensorContextType | undefined>(undefined);

export const SensorProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [sensors, setSensors] = useState<Sensor[]>([]);
  const [selected, setSelected] = useState<Sensor | null>(null);

  return (
    <SensorContext.Provider value={{ sensors, setSensors, selected, setSelected }}>
      {children}
    </SensorContext.Provider>
  );
};

export const useSensorContext = (): SensorContextType => {
  const context = useContext(SensorContext);
  if (!context) throw new Error("useSensorContext must be used within a SensorProvider");
  return context;
};
