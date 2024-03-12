import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { CarForm } from '../components/CarForm';
import { CAR_FORM_PAGE } from '../constants';
import { CARS_URL, AUTH_URL, REGISTER_URL, LOGIN_URL, LOGOUT_URL, USER_PROFILE_URL } from '../constants/urls';

export const CarFormPage = () => {
  return (
    <div>
      <h1>Додати авто</h1>
      <CarForm />
    </div>
  );
};
const CarForm = ({ onSubmit }) => {
  const [brand, setBrand] = useState('');
  const [model, setModel] = useState('');
  const [price, setPrice] = useState('');
  const [currency, setCurrency] = useState('');
  const [region, setRegion] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ brand, model, price, currency, region });
    setBrand('');
    setModel('');
    setPrice('');
    setCurrency('');
    setRegion('');
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="brand">
        <Form.Label>Brand</Form.Label>
        <Form.Control
          type="text"
          value={brand}
          onChange={(e) => setBrand(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="model">
        <Form.Label>Model</Form.Label>
        <Form.Control
          type="text"
          value={model}
          onChange={(e) => setModel(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="price">
        <Form.Label>Price</Form.Label>
        <Form.Control
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="currency">
        <Form.Label>Currency</Form.Label>
        <Form.Control
          as="select"
          value={currency}
          onChange={(e) => setCurrency(e.target.value)}
        >
          <option value="">Select...</option>
          <option value="USD">USD</option>
          <option value="EUR">EUR</option>
          <option value="UAH">UAH</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="region">
        <Form.Label>Region</Form.Label>
        <Form.Control
          as="select"
          value={region}
          onChange={(e) => setRegion(e.target.value)}
        >
          <option value="">Select...</option>
          <option value="USA">USA</option>
          <option value="Europe">Europe</option>
          <option value="Ukraine">UAH</option>
        </Form.Control>
      </Form.Group>
      <Button variant="primary" type="submit">
        Add Car
      </Button>
    </Form>
  );
};

export default CarForm;
