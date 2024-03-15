import { useState, useEffect } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import CarFilter from './CarFilter';
import CarForm from './CarForm';
import CarTable from './CarTable';
import api from './api';

const App = () => {
  const [cars, setCars] = useState([]);
  const [filter, setFilter] = useState({});

  const fetchCars = async () => {
    const response = await api.get('/cars');
    setCars(response.data);
  };

  const handleFilter = (filter) => {
    setFilter(filter);
  };

  const handleSubmit = async (car) => {
    await api.post('/cars', car);
    fetchCars();
  };

  const filteredCars = cars.filter((car) => {
    return (
      (filter.brand ? car.brand === filter.brand : true) &&
      (filter.model ? car.model === filter.model : true) &&
      (filter.region ? car.region === filter.region : true)
    );
  });

  useEffect(() => {
    fetchCars();
  }, []);

  return (
    <Container>
      <Row>
        <Col>
          <h1>Car Marketplace</h1>
        </Col>
      </Row>
      <Row>
        <Col>
          <CarFilter onFilter={handleFilter} />
        </Col>
      </Row>
      <Row>
        <Col>
          <CarForm onSubmit={handleSubmit} />
        </Col>
      </Row>
      <Row>
        <Col>
          <CarTable cars={filteredCars} />
        </Col>
      </Row>
    </Container>
  );
};

export default App;
