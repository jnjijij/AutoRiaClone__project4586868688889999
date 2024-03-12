import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getCars } from '../store/actions/carActions';
import CarFilter from './CarFilter';
import CarItem from './CarItem';
import CarForm from "./CarForm";

const CarList = () => {
  const dispatch = useDispatch();
  const cars = useSelector((state) => state.car.cars);
  const filter = useSelector((state) => state.filter.filter);

  useEffect(() => {
    dispatch(getCars());
  }, [dispatch]);

  const filteredCars = cars.filter((car) => {
    if (filter.brand && car.brand !== filter.brand) return false;
    if (filter.model && car.model !== filter.model) return false;
    if (filter.priceFrom && car.price < filter.priceFrom) return false;
    if (filter.priceTo && car.price > filter.priceTo) return false;
    return true;
  });

  return (
    <div>
      <CarFilter onFilter={(filter) => {
        dispatch(setFilter(filter));
      }} />
      <div className="row">
        {filteredCars.map((car) => (
          <CarItem key={car._id} car={car} />
        ))}
      </div>
    </div>
  );
};

export default CarList;
