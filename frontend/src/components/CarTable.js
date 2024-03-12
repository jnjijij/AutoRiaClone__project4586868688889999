import React from 'react';
import { Table } from 'react-bootstrap';
import CarCard from './CarCard';

const CarTable = ({ cars }) => {
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Brand</th>
          <th>Model</th>
          <th>Price</th>
          <th>Region</th>
        </tr>
      </thead>
      <tbody>
        {cars.map((car) => (
          <tr key={car.id}>
            <td>{car.brand}</td>
            <td>{car.model}</td>
            <td>{car.price} {car.currency}</td>
            <td>{car.region}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};
