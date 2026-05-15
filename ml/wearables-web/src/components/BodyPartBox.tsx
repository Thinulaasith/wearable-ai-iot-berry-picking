import { useMemo } from 'react';
import { Button, Dropdown } from 'react-bootstrap';
import './styles/BodyPartBox.css';

interface Sensor {
    id: string;
    name: string;
    address: string;
    batteryLevel: number;
    chargingStatus: boolean;
    hertzMode: number;
}

interface BodyPartBoxProps {
    part: string;
    imgSrc: string;
    assignedSensor: Sensor | null;
    unassignedSensors: Sensor[];
    onAssign: (sensor: Sensor) => void;
    description: string;
}

const BodyPartBox: React.FC<BodyPartBoxProps> = ({
    part,
    imgSrc,
    assignedSensor,
    unassignedSensors,
    onAssign,
    description
}) => {
    const isAssigned = !!assignedSensor;


    const secondaryText = useMemo(() => {
        if (!isAssigned) return description;
        return `${assignedSensor.name}  •  ${assignedSensor.address}`;
    }, [isAssigned, assignedSensor]);

    return (
        <div className={`body-part-box ${isAssigned ? 'assigned' : 'unassigned'}`}>
            <div className="image-section">
                <img src={imgSrc} height={120} width={120} alt={part} />
            </div>

            <div className="info-section">
                <h5 className="body-part-title">{part.toUpperCase()}</h5>
                <div className="body-part-sub">{secondaryText}</div>
            </div>

            <div className="action-section">
                {isAssigned ? (
                    <Dropdown>
                        <Dropdown.Toggle variant="outline-primary" size="sm">
                            Change
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            {unassignedSensors.length === 0 ? (
                                <Dropdown.Item disabled>No sensors available</Dropdown.Item>
                            ) : (
                                unassignedSensors.map(sensor => (
                                    <Dropdown.Item key={sensor.id} onClick={() => onAssign(sensor)}>
                                        {sensor.name} ({sensor.address})
                                    </Dropdown.Item>
                                ))
                            )}
                        </Dropdown.Menu>
                    </Dropdown>
                ) : (
                    <Dropdown>
                        <Dropdown.Toggle variant="primary" size="sm">
                            Assign
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            {unassignedSensors.length === 0 ? (
                                <Dropdown.Item disabled>No sensors available</Dropdown.Item>
                            ) : (
                                unassignedSensors.map(sensor => (
                                    <Dropdown.Item style={{fontSize: '2rem'}} key={sensor.id} onClick={() => onAssign(sensor)}>
                                        {sensor.name} ({sensor.address})
                                    </Dropdown.Item>
                                ))
                            )}
                        </Dropdown.Menu>
                    </Dropdown>
                )}
            </div>
        </div>
    );
};

export default BodyPartBox;
