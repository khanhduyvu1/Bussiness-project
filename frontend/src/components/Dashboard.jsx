import React, { useState } from 'react';
import { FiMenu } from 'react-icons/fi';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import "../styles/dashboard.css"
function Dashboard() {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => setIsOpen(!isOpen);

    return (
        <div className="dashboard-container">
            <div className="menu-icon" onClick={toggleMenu}>
                <FiMenu size={30} />
            </div>
            <div className={`sidebar ${isOpen ? 'open' : ''}`}>
                <ul>
                    <li><Link to="/items">Items</Link></li>
                    <li><Link to="/cart">Cart</Link></li>
                    <li><Link to="/payment">Payment</Link></li>
                    <li><Link to="/report">Report</Link></li>
                </ul>
            </div>
            <div className="content">
                <div className="user-info">
                    {/* Assume userName and other user details are available */}
                    <p>Welcome, [UserName]</p>
                </div>
                <div className="page-content">
                    {/* Router setup for page content */}
                    <Routes>
                        <Route path="/items" element={<div>Items Page</div>} />
                        <Route path="/cart" element={<div>Cart Page</div>} />
                        <Route path="/payment" element={<div>Payment Page</div>} />
                        <Route path="/report" element={<div>Report Page</div>} />
                    </Routes>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
