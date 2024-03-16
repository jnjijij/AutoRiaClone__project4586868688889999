import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const CarFilter = ({ onFilter }) => {
  const [brand, setBrand] = useState('');
  const [model, setModel] = useState('');
  const [region, setRegion] = useState('');

  const handleFilter = () => {
    onFilter({ brand, model, region });
  };

  return (
    <Form>
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
      <Form.Group controlId="region">
        <Form.Label>Region</Form.Label>
        <Form.Control
          type="text"
          value={region}
          onChange={(e) => setRegion(e.target.value)}
        />
      </Form.Group>
      <Button variant="primary" onClick={handleFilter}>
        Filter
      </Button>
    </Form>
  );
};

const CarFilterPage = () => {
    function useDispatch() {
        return undefined;
    }

    const dispatch = useDispatch();

  const handleFilter = (filter) => {
      function setFilter(filter) {
          return undefined;
      }

      dispatch(setFilter(filter));
  };

  return (
    <div>
      <h1>Car Filter</h1>
      <CarFilter onFilter={handleFilter} />
    </div>
  );
};

export default CarFilterPage;


