import React from 'react';
import { Routes, Route } from 'react-router-dom';

import ItemTable from './Item';
import AddItemForm from './AddNewItem';
import UpdateItemForm from './UpdateItem';

function LinkItems() {
    return (
        <Routes>
            <Route path="/" element={<ItemTable />} />
            <Route path="add_new_item" element={<AddItemForm />} />
            <Route path="update_item" element={<UpdateItemForm />} />
        </Routes>
    );
}

export default LinkItems;