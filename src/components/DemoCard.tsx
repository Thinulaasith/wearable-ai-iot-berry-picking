import type { IconType } from 'react-icons';
import './styles/DemoCard.css';
export interface Demo {
  id: string;
  name: string;
  description: string;
  tagsCount: number;
  icon: IconType;
  iconColor: string;
  activity: string;
}

interface DemoCardProps {
  demo: Demo;
  onSelect?: (id: string) => void; 
}

const DemoCard: React.FC<DemoCardProps> = ({ demo, onSelect }) => (
  <div className="demo-card-container" onClick={() => onSelect?.(demo.id)}>
    <div className="demo-left">

      <demo.icon size={120} color={demo.iconColor}/>
    </div>


    <div className="vertical-divider" />

    <div className="demo-info-section">
      <div className="demo-info-item">
        <span className="label">Demo&nbsp;Name:</span>
        <span className="value">{demo.name}</span>
      </div>

      <div className="demo-info-item">
        <span className="label">Description:</span>
        <span className="value">{demo.description}</span>
      </div>

      <div className="demo-info-item">
        <span className="label">Tags:</span>
        <span className="value">{demo.tagsCount}</span>
      </div>
    </div>
  </div>
);

export default DemoCard;
