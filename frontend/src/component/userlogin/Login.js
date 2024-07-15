import React, { useState } from 'react';
import './Login.css';  // Ensure this CSS file is created for styling
import { loginUser } from './api';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');  // State to handle error messages

    const handleLogin = async (e) => {
        e.preventDefault();
        setError(''); // Clear any existing errors
        try {
            const data = await loginUser(username, password);
            console.log(data); // Handle your token here
            localStorage.setItem('token', data.access_token); // Store token in local storage
            // Redirect or further processing here
        } catch (error) {
            console.error(error);
            setError('Username or password is incorrect');
        }
    };

    return (
        <div className="login-container">
            <h1>eCommerce</h1>
            <form onSubmit={handleLogin} className="login-form">
                <input
                    type="text"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                    placeholder="Username"
                />
                <input
                    type="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                    placeholder="Password"
                />
                <button type="submit">Sign In</button>
                {error && <div className="error-message">{error}</div>}
            </form>
            <p className="register-link">
                Don't have an account? <a href="/register">Register</a>
            </p>
        </div>
    );
}

export default Login;
