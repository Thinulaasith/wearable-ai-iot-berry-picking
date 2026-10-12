import React from "react";
import SensorChart from "../components/Charts/SensorChart";   

const HomePage: React.FC = () => {
  return (
    <div className="p-4 space-y-6">
      <h1 className="text-2xl font-semibold">Home</h1>

      {/* Live acceleration stream */}
      <div className="border rounded-lg shadow-sm p-4">
        <SensorChart />
      </div>
    </div>
  );
};

export default HomePage;
