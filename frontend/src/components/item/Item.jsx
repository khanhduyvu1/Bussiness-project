import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { fetchItemsData } from '../../connection/API';


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
        navigate('/Items/add_new_item');  // Navigate to add new item form
    };

    return (
        <>
            <button onClick={handleAddNewItem}>Create New Item</button>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Description</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Manufacture</th>
                    </tr>
                </thead>
                <tbody>
                    {Array.isArray(items) && items.map(item => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{item.name}</td>
                            <td>{item.category}</td>
                            <td>{item.description}</td>
                            <td>{item.price}</td>
                            <td>{item.quantity}</td>
                            <td>{item.manufacture}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    );
}

export default ItemTable;
