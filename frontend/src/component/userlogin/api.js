import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const createUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/users`, { username, password });
        return response.data;
    } catch (error) {
        throw error.response.data.detail;
    }
};

export const loginUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/token`, new URLSearchParams({ username, password }), {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
        const { access_token } = response.data;
        localStorage.setItem('token', access_token); // Save the token locally
        return access_token;
    } catch (error) {
        throw error.response.data.detail;
    }
};

export const fetchUserInfo = async () => {
    try {
        const token = localStorage.getItem('token');
        const response = await axios.get(`${API_URL}/users`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        return response.data;
    } catch (error) {
        throw error.response.data.detail;
    }
};
