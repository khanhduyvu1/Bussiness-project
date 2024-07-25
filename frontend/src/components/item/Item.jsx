import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { fetchItemsData, deleteItem } from '../../connection/API';
import './Item.css';


function ItemTable() {
    const [items, setItems] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchItems = async () => {
            const result = await fetchItemsData();
            setItems(result);
        };
        fetchItems();
    }, []);

    const handleAddNewItem = () => {
        navigate('/items/add_new_item');  // Navigate to add new item form
    };

    const handleUpdateItem = (item, index) => {
        console.log('Updating item at index:', index, 'Item:', item);
        navigate('/items/update_item');
    }

    const handleDeleteItem = async (itemId) => {
        if (window.confirm("Are you sure you want to delete this item?")) {
            const response = await deleteItem(itemId);
            if (response.ok) {
                alert('Item deleted successfully!');
                setItems(items.filter(item => item.id !== itemId));  // Update the state to remove the deleted item
            } else {
                alert('Failed to delete the item. Please try again.');
            }
        }
    };

    return (
        <>
            <button onClick={handleAddNewItem}>Create New Item</button>
            <table className="table">
                <thead>
                    <tr>
                        <th className="th">ID</th>
                        <th className="th">Name</th>
                        <th className="th">Category</th>
                        <th className="th">Description</th>
                        <th className="th">Price</th>
                        <th className="th">Quantity</th>
                        <th className="th">Manufacture</th>
                        <th className="th">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {Array.isArray(items) && items.map(item => (
                        <tr key={item.id}>
                            <td className="td">{item.id}</td>
                            <td className="td">{item.name}</td>
                            <td className="td">{item.category}</td>
                            <td className="td">{item.description}</td>
                            <td className="td">{item.price}</td>
                            <td className="td">{item.quantity}</td>
                            <td className="td">{item.manufacture}</td>
                            <td className="td">
                                <button onClick={() => handleUpdateItem(item)}>Update</button>
                                <button onClick={() => handleDeleteItem(item.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    );
}

export default ItemTable;
