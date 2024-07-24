// src/components/AddItemForm.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { createItem } from '../../connection/API';


function AddItemForm() {
    const [itemDetails, setItemDetails] = useState({
        id: 0,
        name: '',
        category: '',
        description: '',
        price: 0,
        quantity: 0,
        manufacture: ''
    });
    const navigate = useNavigate();

    const handleChange = (event) => {
        setItemDetails({...itemDetails, [event.target.name]: event.target.value});
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await createItem(itemDetails);
        if (response.ok) {
            alert('Item added successfully!');
            // Reset form to initial state
            setItemDetails({ id: 0 , name: '', category: '', description: '', price: 0, quantity: 0, manufacture: '' });
            navigate('/items')
        } else {
            const errorData = await response.json(); // Assuming the server sends a JSON response with error details
            if (response.status === 400) {
                alert(errorData.detail || 'Item ID is existed.');
            }
        };
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                ID:
                <input type="number" name="id" value={itemDetails.id} onChange={handleChange} />
            </label>
            <br />
            <label>
                Name:
                <input type="text" name="name" value={itemDetails.name} onChange={handleChange} />
            </label>
            <br />
            <label>
                Category:
                <input type="text" name="category" value={itemDetails.category} onChange={handleChange} />
            </label>
            <br />
            <label>
                Description:
                <input type="text" name="description" value={itemDetails.description} onChange={handleChange} />
            </label>
            <br />
            <label>
                Price:
                <input type="number" name="price" value={itemDetails.price} onChange={handleChange} />
            </label>
            <br />
            <label>
                Quantity:
                <input type="number" name="quantity" value={itemDetails.quantity} onChange={handleChange} />
            </label>
            <br />
            <label>
                Manufacture:
                <input type="text" name="manufacture" value={itemDetails.manufacture} onChange={handleChange} />
            </label>
            <br />
            <button type="submit">Add Item</button>
        </form>
    );
}

export default AddItemForm;
