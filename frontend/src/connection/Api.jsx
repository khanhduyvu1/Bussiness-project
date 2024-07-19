import axios from 'axios';
import qs from 'qs';

const API_URL = process.env.REACT_APP_API_URL; // Adjust the port if your FastAPI runs on a different one

export const registerUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/users`, {
            username,
            password
        });
        return response.data;
    } catch (error) {
        console.error('Registration failed:', error.response ? error.response.data : error);
        throw error;
    }
};

export const loginUser = async (username, password) => {
    const data = qs.stringify({
        username: username,
        password: password
    });

    const config = {
        method: 'post',
        url: `${API_URL}/token`,
        headers: { 
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data : data
    };

    try {
        const response = await axios(config);
        return response.data;
    } catch (error) {
        console.error('Login failed:', error.response ? error.response.data : error);
        throw error;
    }
};
