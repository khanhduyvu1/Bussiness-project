import axios from 'axios';
import qs from 'qs';
import { constructQueryParams, constructSearchParams } from './Utils';

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

export const logout = () => {
    localStorage.removeItem('token');
    window.location.href = '/login'; // Redirect to login page
};


export const fetchUserData = async () => {
    try {
        const config = {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`  // Assuming the token is stored in localStorage
            }
        };
        const response = await axios.get(`${API_URL}/users`, config);
        return response.data;
    } catch (error) {
        console.error('Error fetching user data:', error);
        throw error;
    }
};

export const fetchItemsData = async () => {
    return fetch(`${API_URL}/Items`)
      .then(response => {
        return response.json();
      })
};

export const createItem = (itemDetails) => {
    try {
        const token = localStorage.getItem('token');  // Retrieve the token
        return fetch(`${API_URL}/Items`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`  
            },
            body: JSON.stringify(itemDetails)
    });  
    } catch(error) {
        throw error;
    }
    
};

export const searchItem = async (searchParams) => {
    try {
        const token = localStorage.getItem('token');
        const queryParams = constructSearchParams(searchParams);
        const response = await fetch(`${API_URL}/Items/search?${queryParams}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
        });

        if (!response.ok) {
            throw new Error('No items found matching the criteria');
        }

        const data = await response.json();
        console.log('API response data:', data); // Add logging here
        return Array.isArray(data) ? data : [];
    } catch (error) {
        console.error('API error:', error); // Add logging here
        throw error;
    }
};

export const updateItem = (updatedData) => {
    const token = localStorage.getItem('token');
    const queryParams = constructQueryParams(updatedData);

    return fetch(`${API_URL}/Items/update?${queryParams}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
    }); 
    
};

export const deleteItem = async (itemId) => {
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_URL}/Items/delete?item_id=${itemId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });
        return response;
    } catch (error) {
        console.error('Failed to delete the item:', error);
        return null; 
    }
};