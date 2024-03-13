import { cars } from '../data/cars';

export const getCars = () => {
  return cars;
};

export const getCarById = (id) => {
  return cars.find((car) => car.id === id);
};

export const addCar = (car) => {
  cars.push(car);
};

export const updateCar = (id, updatedCar) => {
  const car = getCarById(id);
  Object.assign(car, updatedCar);
};

export const deleteCar = (id) => {
  const carIndex = cars.findIndex((car) => car.id === id);
  cars.splice(carIndex, 1);
};