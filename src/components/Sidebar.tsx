import React from 'react';
import { NavLink } from 'react-router-dom';
import { FiHome, FiMic, FiFolder, FiBarChart2, FiSettings } from 'react-icons/fi';
import { TbDeviceAirtag } from 'react-icons/tb';

interface SidebarLinkProps {
  to: string;
  label: string;
  icon: React.ComponentType<any>;
}

const SidebarLink: React.FC<SidebarLinkProps> = ({ to, label, icon: Icon }) => (
  <NavLink
    to={to}
    end
    className="d-flex align-items-center p-4 text-decoration-none"
    style={({ isActive }) => ({
      color: isActive ? '#ffffff' : '#adb5bd',
      backgroundColor: isActive ? '#495057' : 'transparent',
    })}
  >
    <Icon className="me-4" size={25} />
    <span>{label}</span>
  </NavLink>
);

/**
 * Sidebar – fixed dark vertical navigation bar.
 */
const Sidebar: React.FC = () => (
  <div className="bg-dark d-flex flex-column justify-content-between min-vh-100" style={{ width: '100%', fontSize: '20px' }}>
    <div>
      <SidebarLink to="/" icon={FiHome} label="Home" />
      <SidebarLink to="/start" icon={FiMic} label="Start Recording" />
      <SidebarLink to="/viewrecording" icon={FiFolder} label="View Recording" />
      <SidebarLink to="/analytics" icon={FiBarChart2} label="Analytics" />
      <SidebarLink to="/managewearables" icon={TbDeviceAirtag} label="Manage Wearables" />
      <SidebarLink to="/demomenu" icon={TbDeviceAirtag} label="Demo" />
    </div>
    <div>
      <SidebarLink to="/settings" icon={FiSettings} label="Settings" />
    </div>
  </div>
);

export default Sidebar;