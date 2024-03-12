import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CarBrands from './components/CarBrands';
import CarModels from './components/CarModels';
import CarPrices from './components/CarPrices';
import React from 'react';
import { LoginForm } from '../components/LoginForm';
import { CarsPage } from '../pages/CarsPage';
import { LoginPage } from '../pages/LoginPage';
import { CarFormPage } from '../pages/CarFormPage';
import { CarFilterPage } from '../pages/CarFilterPage';
import { MainLayout } from '../components/MainLayout';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/car_brands" component={CarBrands} />
        <Route path="/car_models" component={CarModels} />
        <Route path="/car_prices" component={CarPrices} />
          <Route path="/car-form" component={() => <MainLayout><CarFormPage /></MainLayout>} />
        <Route path="/car-filter" component={() => <MainLayout><CarFilterPage /></MainLayout>} />
          <Route path="/" exact component={CarsPage} />
          <Route path="/login" component={LoginPage} />
        <Route path="/car-form" component={() => <MainLayout><CarFormPage /></MainLayout>} />
        <Route path="/car-filter" component={() => <MainLayout><CarFilterPage /></MainLayout>} />
      </Switch>
    </Router>
  );
}

export default App;
