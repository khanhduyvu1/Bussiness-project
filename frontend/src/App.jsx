import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';

import Login from './components/user/Login';
import Register from './components/user/Register';
import Dashboard from './components/Dashboard';
import LinkItems from './components/item/Link';
import Carts from './components/cart/Cart';
import Payments from './components/payment/Payment';
import Reports from './components/report/Report';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate replace to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard/*" element={<Dashboard />} />
        <Route path="/items/*" element={<LinkItems />} />
        <Route path="/cart" element={<Carts />} />
        <Route path="/payment" element={<Payments />} />
        <Route path="/report" element={<Reports />} />
      </Routes>
    </Router>
  );
}

export default App;
