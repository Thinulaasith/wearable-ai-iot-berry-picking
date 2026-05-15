import { useEffect, useMemo, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import type { Demo, BodyPartKey } from '../data/demos';
import { demos } from '../data/demos';

import Card from 'react-bootstrap/Card';
import { Container, Row, Col, Form, Button, ToggleButton } from 'react-bootstrap';

import { useSensorContext } from '../context/SensorContext';
import BodyPartBox from '../components/BodyPartBox';
import upperArmImg from '/images/upper-arm.png';
import upperBackImg from '/images/upper-back.png';
import wristImg from '/images/wrist.png';
import legImg from '/images/leg.png';
import placementImg from '/images/demo-placement.png';
import RMSChart from '../components/RMSChart';

import '../styles/DemoPage.css';

// ---------------- Types ----------------
interface ClassificationPoint {
    time: number;
    action: number;
    ts?: number;
}
export interface ChartPoint {
    ts: number;
    action: number;
}
interface Sensor {
    id: string;
    name: string;
    address: string;
    batteryLevel: number;
    chargingStatus: boolean;
    hertzMode: number;
}

const Stage = { Assign: 1, LiveGraphs: 2, Summary: 3 } as const;
type Stage = (typeof Stage)[keyof typeof Stage];

// ---------------- Constants ----------------
const ACTIVITY_NAMES: Record<number, string> = {
    1: 'Bending',
    2: 'Idle',
    3: 'Picking',
    4: 'Pushing',
};

// Canonical keys used by your demos data (imported from ../data/demos)
// type BodyPartKey = "forearm" | "upper_back" | "upper_leg" | "ankle";

// Map body-part key -> pretty label + single image used by BodyPartBox
const BODY_PART_META: Record<BodyPartKey, { label: string; img: string; desc: string }> = {
    forearm: {
        label: 'Forearm (dominant)',
        img: upperArmImg,
        desc: 'Place on the back of the dominant forearm.',
    },
    upper_back: {
        label: 'Upper Back',
        img: upperBackImg,
        desc: 'Place on the upper back between the shoulder blades.',
    },
    upper_leg: {
        label: 'Upper Leg (thigh)',
        img: legImg,
        desc: 'Place on the outer thigh of the right leg.',
    },
    ankle: {
        label: 'Ankle',
        img: legImg,
        desc: 'Place just above the lateral ankle bone.',
    },
    upper_arm: {
        label: 'Upper Arm (dominant)',
        img: upperArmImg,
        desc: 'Place on the back of the dominant upper arm.',
    },
    wrist: {
        label: 'Wrist (dominant)',
        img: wristImg,
        desc: 'Place on the outside of the dominant wrist.',
    },
};

type Assignment = { body_part: BodyPartKey; sensor: Sensor | null };

// ---------------- Component ----------------
const DemoPage: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const demo: Demo | null = useMemo(() => demos.find((d) => d.id === id) ?? null, [id]);

    const timeoutRef = useRef<NodeJS.Timeout | null>(null);
    const { sensors } = useSensorContext();

    const [viewClassification, setViewClassification] = useState(false);
    const [stage, setStage] = useState<Stage>(Stage.Assign);
    const [demoStartTime, setDemoStartTime] = useState<number | null>(null);

    const [models, setModels] = useState<string[]>([]);
    const [selectedModel, setSelectedModel] = useState<string>('');

    // Determine fixed parts from the demo list (first card uses [0], second uses [1])
    const partA: BodyPartKey | null = useMemo(() => {
        if (!demo?.bodyParts?.[0]) return null;
        return demo.bodyParts[0] as BodyPartKey;
    }, [demo]);

    const partB: BodyPartKey | null = useMemo(() => {
        if (!demo?.bodyParts?.[1]) return null;
        return demo.bodyParts[1] as BodyPartKey;
    }, [demo]);

    // Two fixed slots that match your two BodyPartBox “cards”
    const [slots, setSlots] = useState<Record<'A' | 'B', Assignment> | null>(null);
    useEffect(() => {
        if (!partA || !partB) return;
        setSlots({
            A: { body_part: partA, sensor: null },
            B: { body_part: partB, sensor: null },
        });
    }, [partA, partB]);

    const [demoLength, setDemoLength] = useState<number>(60);
    const [classificationData, setClassificationData] = useState<ChartPoint[]>([]);
    const [actionCode, setActionCode] = useState<number | null>(null);

    // Available sensors (exclude those already assigned)
    const assignedIds = useMemo(() => {
        if (!slots) return [] as string[];
        return (['A', 'B'] as const).map((k) => slots[k].sensor?.id).filter(Boolean) as string[];
    }, [slots]);

    const unassignedSensors = useMemo(
        () => sensors.filter((s) => !assignedIds.includes(s.id)),
        [sensors, assignedIds],
    );

    const setSlotSensor = (slot: 'A' | 'B', sensor: Sensor) =>
        setSlots((prev) => (prev ? { ...prev, [slot]: { ...prev[slot], sensor } } : prev));

    // ---------------- Controls ----------------
    const handleStart = () => {
        if (!demo || !slots) {
            alert('Demo not ready.');
            return;
        }

        const chosen = (['A', 'B'] as const)
            .map((k) => slots[k])
            .filter((s): s is { body_part: BodyPartKey; sensor: Sensor } => !!s.sensor);

        if (chosen.length !== 2) {
            alert('Assign a sensor to both body parts.');
            return;
        }
        if (!Number.isFinite(demoLength) || demoLength <= 0) {
            alert('Demo length must be a positive integer.');
            return;
        }

        setDemoStartTime(Date.now());
        setActionCode(null);
        setClassificationData([]);
        setStage(Stage.LiveGraphs);

        fetch('http://localhost:5000/start-multiple', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sensors: chosen.map((c) => ({
                    sensor_id: c.sensor.address,
                    body_part: c.body_part,
                })),
                activity: demo.activity,
                duration: demoLength,
                model_name: selectedModel,
            }),
        })
            .then((r) => r.json())
            .catch((err) => console.error('Failed to start sensors:', err));
    };

    const handleRedo = () => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
            timeoutRef.current = null;
        }
        if (!demo || !slots) return;

        const chosen = (['A', 'B'] as const)
            .map((k) => slots[k])
            .filter((s): s is { body_part: BodyPartKey; sensor: Sensor } => !!s.sensor);

        if (chosen.length !== 2) {
            alert('Assign a sensor to both body parts.');
            return;
        }

        setDemoStartTime(Date.now());
        setActionCode(null);
        setClassificationData([]);
        setStage(Stage.LiveGraphs);
        setViewClassification(false);

        fetch('http://localhost:5000/start-multiple', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sensors: (['A', 'B'] as const).map((k) => ({
                    sensor_id: slots[k]!.sensor!.address,
                    body_part: slots[k]!.body_part,
                    slot: k,
                })),
                activity: demo.activity,
                duration: demoLength,
                model_name: selectedModel,
            }),
        })
            .then((r) => r.json())
            .catch((err) => console.error('Failed to restart demo:', err));
    };

    const handleStop = () => {
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
            timeoutRef.current = null;
        }

        fetch('http://localhost:5000/stop-all', { method: 'POST' })
            .then((res) => res.json())
            .then(() => setStage(Stage.Summary))
            .catch((err) => console.error('Failed to stop sensors:', err));
    };

    useEffect(() => {
        const fetchClassification = async () => {
            try {
                const point: ClassificationPoint | undefined = await fetch(
                    'http://localhost:5000/classification',
                ).then((r) => r.json());
                if (!point || point.action == null) {
                    setActionCode(null);
                    return;
                }

                setActionCode(point.action);
                setClassificationData((prev) => {
                    const seen = new Set(prev.map((p) => p.ts));
                    const ts =
                        (point.ts as number) ??
                        (typeof point.time === 'number' ? point.time : Date.now());
                    if (seen.has(ts)) return prev;
                    return [...prev, { ts, ...point }].slice(-60);
                });
            } catch {
                setActionCode(null);
            }
        };

        fetchClassification();
        const id = setInterval(fetchClassification, 300);
        return () => clearInterval(id);
    }, []);

    useEffect(() => {
        if (stage !== Stage.LiveGraphs || !demoStartTime) return;
        if (timeoutRef.current) clearTimeout(timeoutRef.current);
        timeoutRef.current = setTimeout(() => {
            setStage(Stage.Summary);
            timeoutRef.current = null;
        }, demoLength * 1000);
        return () => {
            if (timeoutRef.current) {
                clearTimeout(timeoutRef.current);
                timeoutRef.current = null;
            }
        };
    }, [stage, demoStartTime, demoLength]);

    useEffect(() => {
        if (!demo?.activity) {
            setModels([]);
            setSelectedModel('');
            return;
        }

        fetch(`http://localhost:5000/models?activity=${encodeURIComponent(demo.activity)}`)
            .then((r) => r.json())
            .then((res) => {
                const list = Array.isArray(res.models) ? res.models : [];
                setModels(list);
                setSelectedModel((prev) => (prev && list.includes(prev) ? prev : (list[0] ?? '')));
            })
            .catch((err) => {
                console.error('Failed to load models:', err);
                setModels([]);
                setSelectedModel('');
            });
    }, [demo?.activity]);

    const statusLabel = actionCode === null ? 'LOADING' : ACTIVITY_NAMES[actionCode];

    if (!demo) return <p className="error-message">Demo not found</p>;
    if (!partA || !partB || !slots)
        return <p className="error-message">Demo body parts not configured</p>;

    const metaA = BODY_PART_META[partA];
    const metaB = BODY_PART_META[partB];

    return (
        <Container fluid className="demo-container p-4" style={{ fontSize: '30px' }}>
            <div className="demo-header">
                <h1>{demo.name}</h1>
                <hr />
                <p className="demo-description">{demo.description}</p>
            </div>

            {stage === Stage.Assign && (
                <>
                    <Button
                        variant="secondary"
                        onClick={() => navigate('/demomenu')}
                        className="mb-3"
                    >
                        ← Back to Menu
                    </Button>

                    <h4>Assign Sensors to Body</h4>
                    <Row className="justify-content-center">
                        <Col md={4}>
                            <img
                                src={placementImg}
                                alt="Sensor placement"
                                style={{ width: '100%', height: 'auto', display: 'block' }}
                            />
                        </Col>
                    </Row>

                    <Row className="mt-3">
                        <Col md={6} className="mt-3">
                            {/* First BodyPartBox = demo.bodyParts[0] */}
                            <BodyPartBox
                                part={metaA.label}
                                imgSrc={metaA.img}
                                assignedSensor={slots.A.sensor}
                                unassignedSensors={unassignedSensors}
                                onAssign={(s) => setSlotSensor('A', s)}
                                description={metaA.desc}
                            />
                        </Col>

                        <Col md={6} className="mt-3">
                            {/* Second BodyPartBox = demo.bodyParts[1] */}
                            <BodyPartBox
                                part={metaB.label}
                                imgSrc={metaB.img}
                                assignedSensor={slots.B.sensor}
                                unassignedSensors={unassignedSensors}
                                onAssign={(s) => setSlotSensor('B', s)}
                                description={metaB.desc}
                            />
                        </Col>
                    </Row>

                    <Row className="mt-4">
                        <Col md={4} className="mx-auto">
                            <Form.Group controlId="modelSelect">
                                <Form.Label className="fw-bold">Model</Form.Label>
                                <Form.Select
                                    value={selectedModel}
                                    onChange={(e) => setSelectedModel(e.target.value)}
                                    disabled={!models.length}
                                >
                                    {models.length === 0 ? (
                                        <option value="">No models found</option>
                                    ) : (
                                        models.map((m) => (
                                            <option key={m} value={m}>
                                                {m}
                                            </option>
                                        ))
                                    )}
                                </Form.Select>
                            </Form.Group>
                        </Col>
                    </Row>

                    <Row className="mt-4">
                        <Col md={4} className="mx-auto">
                            <Form.Group controlId="demoLength">
                                <Form.Label className="fw-bold">Demo length (seconds)</Form.Label>
                                <Form.Select
                                    value={demoLength}
                                    onChange={(e) => setDemoLength(Number(e.target.value))}
                                >
                                    {[15, 30, 45, 60, 75, 90, 105, 120].map((sec) => (
                                        <option key={sec} value={sec}>
                                            {sec}
                                        </option>
                                    ))}
                                </Form.Select>
                            </Form.Group>
                        </Col>
                    </Row>

                    <Row className="mt-4">
                        <Col className="d-flex justify-content-center">
                            <Button variant="success" onClick={handleStart}>
                                Start Demo
                            </Button>
                        </Col>
                    </Row>
                </>
            )}

            {stage === Stage.LiveGraphs && (
                <>
                    <Row className="mt-4">
                        {slots.A.sensor && (
                            <Col md={6}>
                                <RMSChart sensor={slots.A.sensor} />
                            </Col>
                        )}
                        {slots.B.sensor && (
                            <Col md={6}>
                                <RMSChart sensor={slots.B.sensor} />
                            </Col>
                        )}
                    </Row>

                    <Row className="mt-3">
                        <Col className="d-flex justify-content-center">
                            <Card
                                className="status-card"
                                style={{
                                    backgroundColor:
                                        actionCode === null
                                            ? '#6c757d' // gray for LOADING
                                            : actionCode === 1
                                              ? '#0d6efd' // Bending → blue
                                              : actionCode === 2
                                                ? '#6c757d' // Idle → gray
                                                : actionCode === 3
                                                  ? '#ffc107' // Picking → yellow
                                                  : '#dc3545', // Pushing → red
                                }}
                                text="white"
                            >
                                <Card.Body className="d-flex justify-content-center align-items-center">
                                    <span className="fw-bold display-3 m-0">{statusLabel}</span>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>

                    <Row className="mt-3">
                        <Col className="d-flex justify-content-center">
                            <ToggleButton
                                id="toggle-view-classification"
                                type="checkbox"
                                variant="outline-primary"
                                checked={viewClassification}
                                value="view"
                                style={{ fontSize: '30px' }}
                                onChange={(e) => setViewClassification(e.currentTarget.checked)}
                            >
                                {viewClassification ? 'Hide classification' : 'Show classification'}
                            </ToggleButton>
                        </Col>
                    </Row>

                    <Row className="mt-5">
                        <Col className="d-flex justify-content-center">
                            <Button variant="danger" onClick={handleStop}>
                                Stop Demo
                            </Button>
                        </Col>
                    </Row>
                </>
            )}
        </Container>
    );
};

export default DemoPage;
