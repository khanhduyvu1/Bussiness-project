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
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
      })  
    }
// export const createItem = (itemDetails) => {
//     return fetch(`${API_URL}/Items`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(itemDetails)
//     });
// };

// export const updateItem = (itemId, itemDetails) => {
//     return fetch(`${API_URL}/Items/update/${itemId}`, {
//         method: 'PUT',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(itemDetails)
//     });
// };

// export const deleteItem = (itemId) => {
//     return fetch(`${API_URL}/Items/delete/${itemId}`, {
//         method: 'DELETE'
//     });
// };