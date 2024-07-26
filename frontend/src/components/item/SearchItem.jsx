import React, { useState, } from 'react';
//import { useNavigate } from 'react-router-dom';

import { searchItem } from '../../connection/API';

function SearchComponent() {
    const [name, setName] = useState('');
    const [category, setCategory] = useState('');
    const [manufacture, setManufacture] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');
    //const navigate = useNavigate();

    const handleSearch = async () => {
        try {
            const searchParams = { name, category, manufacture };
            const data = await searchItem(searchParams);
            setResults(Array.isArray(data) ? data : []);
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div>
            <h1>Search Items</h1>
            <input
                type="text"
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                type="text"
                placeholder="Category"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
            />
            <input
                type="text"
                placeholder="Manufacture"
                value={manufacture}
                onChange={(e) => setManufacture(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
            {error && <p>{error}</p>}
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
                    {results.map((item) => (
                        <tr key={item.id}>
                            <td className="td">{item.id}</td>
                            <td className="td">{item.name}</td>
                            <td className="td">{item.category}</td>
                            <td className="td">{item.description}</td>
                            <td className="td">{item.price}</td>
                            <td className="td">{item.quantity}</td>
                            <td className="td">{item.manufacture}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default SearchComponent;
