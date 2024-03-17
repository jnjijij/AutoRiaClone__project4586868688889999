# Car Management System

This project is a simple car management system with a backend API built using Django and a frontend client built using React.

## Backend

The backend API is built using Django and provides endpoints for managing cars and their advertisements.

### Installation and Usage

1. Navigate to the `backend` directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the backend server using `python manage.py runserver`.

### Endpoints

- GET /cars: Retrieve a list of all cars.
- GET /cars/<car_id>: Retrieve details of a specific car.
- POST /cars: Add a new car to the system.
- PUT /cars/<car_id>: Update details of a specific car.
- DELETE /cars/<car_id>: Delete a specific car.

## Frontend

The frontend client is built using React and provides a user interface for interacting with the car management system.

### Installation and Usage

1. Navigate to the `frontend` directory.
2. Install the required dependencies using `npm install`.
3. Start the frontend client using `npm start`.

### Features

- View a list of all cars.
- View details of a specific car.
- Add a new car to the system.
- Update details of a specific car.
- Delete a specific car.

## Client

The client interacts with the backend API to provide a seamless user experience. It is built using React and communicates with the backend using HTTP requests.

### Usage

The client provides a user-friendly interface for accessing the car management system. It communicates with the backend API to perform CRUD operations on cars.

- Access the home page to view a list of all cars.
- View a specific car by navigating to /car/<car_id>.
- Edit a car's details by navigating to /car/<car_id>/edit.
- Retrieve information about a car's advertisements by navigating to /car/<car_id>/ads_info.

## Dependencies

### Backend

- Django
- Django-Rest-Framework
- Django-SQLAlchemy

### Frontend

- React
- Axios (for making HTTP requests)

### Database

The backend application uses a SQLite database located at backend/cars.db.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

#127.0.0.1 is the localhost IP address, and 8000 is the default port number for the Django development server. If the server is running on a different port, replace 8000 with the appropriate port number.