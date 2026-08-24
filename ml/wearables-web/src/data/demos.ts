import { FaPeopleCarryBox, FaKeyboard, FaBox, FaRaspberryPi } from 'react-icons/fa6';
import { MdPrecisionManufacturing } from 'react-icons/md';
import { IoBody } from 'react-icons/io5';
import { TfiSpray } from 'react-icons/tfi';

// New: canonical keys for body parts you support
export type BodyPartKey =
    | 'forearm'
    | 'upper_back'
    | 'upper_leg'
    | 'ankle'
    | 'upper_arm'
    | 'wrist'
    | 'left_wrist'
    | 'right_wrist';

export type Demo = {
    id: string;
    name: string;
    description: string;
    tagsCount: number; // can keep for UI badges if you want
    icon: any;
    iconColor: string;
    activity: string;
    /** NEW: which three body parts this demo uses (always 3 for your flow) */
    bodyParts: [BodyPartKey, BodyPartKey, BodyPartKey];
};

export const demos: Demo[] = [
    {
        id: '7',
        name: 'Berry Picking',
        description: 'Classify Berry Picking Activities',
        tagsCount: 2,
        icon: FaRaspberryPi,
        iconColor: 'red',
        activity: 'berry',
        bodyParts: ['left_wrist', 'right_wrist', 'upper_leg'],
    },
];
