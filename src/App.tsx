import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, Row, Col } from 'react-bootstrap';
import Sidebar from './components/Sidebar';
import HomePage from './pages/Home';
import 'bootstrap/dist/css/bootstrap.min.css';
import './app.css';
import ViewRecordingPage from './pages/ViewRecording';
import ManageWearablesPage from './pages/ManageWearables';
import DemoMenuPage from './pages/DemoMenu';

import { SensorProvider } from './context/SensorContext';
import DemoPage from './pages/DemoPage';

import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

const Page: React.FC<{ title: string }> = ({ title }) => (
  <div className="p-4">
    <h1>{title}</h1>
  </div>
);


const App: React.FC = () => {
  return (
    <DndProvider backend={HTML5Backend}>


      <SensorProvider>
        <Router>
          <Container fluid className="min-vh-100 d-flex flex-column" style={{ backgroundColor: '#2a2f37', color: '#f1f3f5' }}>
            <Row className="flex-grow-1 w-100">

              <Col xs={2} className="p-0 bg-dark min-vh-100">
                <Sidebar />
              </Col>

              <Col xs={10} className="overflow-auto min-vh-100">
                <Routes>
                  <Route path="/" element={<HomePage />} />
                  <Route path="/page2" element={<Page title="Page 2" />} />
                  <Route path="/viewrecording" element={<ViewRecordingPage />} />
                  <Route path="/managewearables" element={<ManageWearablesPage />} />
                  <Route path="/demomenu" element={<DemoMenuPage />} />
                  <Route path="/demo/:id" element={<DemoPage />} />

                </Routes>
              </Col>
            </Row>
          </Container>
        </Router>
      </SensorProvider>
    </DndProvider>
  );
};

export default App;
