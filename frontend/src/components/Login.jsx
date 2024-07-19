import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/loginscreen.css';
import { loginUser } from '../connection/Api';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await loginUser(username, password);
            console.log('Login successful:', response.data);
            // Navigate to another route on success or handle login logic
            localStorage.setItem('token', response.access_token);
            navigate('/dashboard');
        } catch (error) {
            console.error('Login error:', error.response || error);
            if (error.response && error.response.status === 401) {
                setError('Wrong username or password');
            }
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            {error && <p className="error">{error}</p>}
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
