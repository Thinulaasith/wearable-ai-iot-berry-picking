import { FaBatteryHalf, FaChargingStation } from "react-icons/fa";
import { MdBatteryChargingFull, MdBatteryStd } from "react-icons/md";
import './styles/SensorCard.css';

interface Sensor {
    id: string;
    name: string;
    address: string;
    batteryLevel: number;
    chargingStatus: boolean;
    hertzMode: number;
}

interface SensorCardProps {
    sensor: Sensor;
    onViewRMS?: () => void;
}

const SensorCard: React.FC<SensorCardProps> = ({ sensor, onViewRMS }) => {
    return (
        <div className="sensor-card-container">
            <div className="sensor-left">
                <img src="src/assets/movella_dot.webp" height={90} width={90} alt="sensor" />
            </div>

            <div className="sensor-center">
                <div className="sensor-id-section">
                    <span className="tag-label">TAG:</span>
                    <span className="sensor-id">{sensor.id}</span>
                </div>

                <div className="vertical-divider" />

                <div className="sensor-info-section">
                    <div className="sensor-info-item">
                        <span className="label">Address:</span>
                        <span className="value">{sensor.address}</span>
                    </div>
                    <div className="sensor-info-item">
                        <span className="label">Battery:</span>
                        <span className="value icon-text">
                            {sensor.batteryLevel}%{" "}
                            {sensor.batteryLevel > 70 ? <MdBatteryStd size={22} /> : <FaBatteryHalf size={22} />}
                        </span>
                    </div>
                    <div className="sensor-info-item">
                        <span className="label">Charging:</span>
                        <span className="value icon-text">
                            {sensor.chargingStatus ? (
                                <MdBatteryChargingFull size={22} className="charging" />
                            ) : (
                                <FaChargingStation size={22} className="not-charging" />
                            )}
                        </span>
                    </div>
                    <div className="sensor-info-item">
                        <span className="label">Hertz:</span>
                        <span className="value icon-text">
                            {sensor.hertzMode}
                        </span>
                    </div>
                </div>
            </div>

            {/* Right: Actions */}
            <div className="sensor-actions">
                <button className="sensor-btn" onClick={onViewRMS}>
                    View RMS
                </button>
                <button className="sensor-btn">View x, y, z</button>
            </div>
        </div>
    );
};


export default SensorCard;
