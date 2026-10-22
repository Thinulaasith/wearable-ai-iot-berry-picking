import DemoCard from "../components/DemoCard";
import { demos } from "../data/demos";
import { useNavigate } from "react-router-dom";

import "../styles/DemoMenu.css";

const DemoMenuPage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="manage-demos-container">
      <h1 className="manage-demos-title">Demo Programs</h1>
      <hr className="manage-demos-divider" />
      <p className="manage-demos-text">Please select a Demo to run from the list below</p>

      <div className="demo-list">
        {demos.map((demo) => (
          <DemoCard key={demo.id} demo={demo} onSelect={() => navigate(`/demo/${demo.id}`)} />
        ))}
      </div>
    </div>
  );
};

export default DemoMenuPage;
