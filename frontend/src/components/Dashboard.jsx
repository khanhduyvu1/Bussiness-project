import React, { useState, useEffect } from 'react';
import { FiMenu } from 'react-icons/fi';
// eslint-disable-next-line
import { Link } from 'react-router-dom';

import { fetchUserData } from '../connection/API';
//import "../styles/dashboard.css"

function Dashboard() {
    const [isOpen, setIsOpen] = useState(false);
    const [username, setUsername] = useState('');

    const toggleMenu = () => setIsOpen(!isOpen);

    useEffect(() => {
        const getUserData = async () => {
            try {
                const userData = await fetchUserData();
                setUsername(userData.User.username); // Adjust according to your response structure
            } catch (error) {
                console.error('Failed to fetch user:', error);
                setUsername('Error'); // Fallback username
            }
        };

        getUserData();
    }, []);

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
                    <p>Welcome,{username}</p>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
