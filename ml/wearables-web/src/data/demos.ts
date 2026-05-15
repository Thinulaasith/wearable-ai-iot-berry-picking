import { FaPeopleCarryBox, FaKeyboard, FaBox, FaRaspberryPi } from 'react-icons/fa6';
import { MdPrecisionManufacturing } from 'react-icons/md';
import { IoBody } from 'react-icons/io5';
import { TfiSpray } from 'react-icons/tfi';

// New: canonical keys for body parts you support
export type BodyPartKey = 'forearm' | 'upper_back' | 'upper_leg' | 'ankle' | 'upper_arm' | 'wrist';

export type Demo = {
    id: string;
    name: string;
    description: string;
    tagsCount: number; // can keep for UI badges if you want
    icon: any;
    iconColor: string;
    activity: string;
    /** NEW: which two body parts this demo uses (always 2 for your flow) */
    bodyParts: [BodyPartKey, BodyPartKey];
};

export const demos: Demo[] = [
    {
        id: '1',
        name: 'Lifting Box',
        description: 'Ergonomic lift of a 0.5kg box from floor.',
        tagsCount: 2,
        icon: FaPeopleCarryBox,
        iconColor: 'white',
        activity: 'pickup',
        bodyParts: ['forearm', 'upper_leg'],
    },
    {
        id: '2',
        name: 'Placing Box On Shelf',
        description: 'Lifting box from ground and placing on shelf',
        tagsCount: 2,
        icon: FaBox,
        iconColor: 'brown',
        activity: 'shelf',
        bodyParts: ['forearm', 'upper_arm'],
    },
    {
        id: '3',
        name: 'Spraying Water',
        description: 'Spraying water mist using spray gun',
        tagsCount: 2,
        icon: TfiSpray,
        iconColor: 'green',
        activity: 'spray',
        bodyParts: ['forearm', 'upper_back'],
    },
    {
        id: '4',
        name: 'Twisting Body',
        description: 'Twisting while seated at desk',
        tagsCount: 2,
        icon: IoBody,
        iconColor: 'lightPink',
        activity: 'twisting',
        bodyParts: ['upper_back', 'upper_leg'],
    },
    {
        id: '5',
        name: 'Circuit Assembly',
        description: 'Fine-motor PCB assembly.',
        tagsCount: 2,
        icon: MdPrecisionManufacturing,
        iconColor: 'grey',
        activity: 'circuit',
        bodyParts: ['forearm', 'upper_back'],
    },
    {
        id: '6',
        name: 'Keyboard Typing',
        description: 'Speed-typing posture assessment.',
        tagsCount: 2,
        icon: FaKeyboard,
        iconColor: 'orange',
        activity: 'keyboard',
        bodyParts: ['forearm', 'upper_back'],
    },
    {
        id: '7',
        name: 'Berry Picking',
        description: 'Classify Berry Picking Activities',
        tagsCount: 2,
        icon: FaRaspberryPi,
        iconColor: 'red',
        activity: 'berry',
        bodyParts: ['wrist', 'upper_leg'],
    },
];
