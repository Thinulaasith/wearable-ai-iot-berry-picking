import { FaRaspberryPi } from 'react-icons/fa6';

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
    tagsCount: number;
    icon: any;
    iconColor: string;
    activity: string;
    bodyParts: [BodyPartKey, BodyPartKey];
};

export const demos: Demo[] = [
    {
        id: '1',
        name: 'Berry Picking',
        description: 'Classify Berry Picking Activities',
        tagsCount: 2,
        icon: FaRaspberryPi,
        iconColor: 'red',
        activity: 'berry',
        bodyParts: ['wrist', 'upper_leg'],
    },
];
