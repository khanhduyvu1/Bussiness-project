import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ItemTable from './Item';
import AddItem from './AddNewItem';

function LinkItems() {
    return (
        <Routes>
            <Route path="/" element={<ItemTable />} />
            <Route path="add_new_item" element={<AddItem />} />
        </Routes>
    );
}

export default LinkItems;