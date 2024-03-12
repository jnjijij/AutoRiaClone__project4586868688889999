import React from 'react';
import { Card, Button } from 'react-bootstrap';

const CarCard = ({ car }) => {
  return (
    <Card>
      <Card.Body>
        <Card.Title>{car.brand} {car.model}</Card.Title>
        <Card.Text>
          Price: {car.price} {car.currency}
        </Card.Text>
        <Card.Text>
          Region: {car.region}
        </Card.Text>
        <Button variant="primary">View Details</Button>
      </Card.Body>
    </Card>
  );
};

export default CarCard;
