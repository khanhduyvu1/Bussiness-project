import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../styles/loginscreen.css';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/login', {
                username,
                password
            });
            console.log('Login successful:', response.data);
            // Navigate to another route on success or handle login logic
            navigate('/dashboard');
        } catch (error) {
            console.error('Login error:', error.response || error);
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin} className="login-form">
                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />

                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />

                <button type="submit">Sign In</button>
            </form>
            <p>
                Don't have an account? <button onClick={() => navigate('/Register')}>Register</button>
            </p>
        </div>
    );
}

export default Login;
