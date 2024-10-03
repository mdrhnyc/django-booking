# Django Booking System Backend

### Project Overview
A simple **Django backend** for managing bookings, services, providers, and customers. The project offers API endpoints to handle the core functionality of a booking system, along with an integrated **Django Admin interface** for easy management.

### Technologies Used
- **Django** for backend logic
- **Django Rest Framework (DRF)** for API creation
- **SQLite** as the default database (can be changed if needed)

### Setup Instructions

1. **Clone the repository** and navigate to the project directory:
   ```
   git clone https://github.com/mdrhnyc/django-booking.git
   cd spa_booking
   ```
2. **Set up the virtual environment** and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run database migrations** (using SQLite):
   ```
   python manage.py migrate
   ```
4. **Create a superuser for accessing the admin interface**:
   ```
   python manage.py createsuperuser
   ```
5. **Run the development server**:
   ```
   python manage.py runserver
   ```
6. **Access the Django Admin Interface**: You can access the admin interface at:
   ```
   http://127.0.0.1:8000/admin/
   ```

### API Endpoints

#### Services
- **GET** `/api/services/`: List all services
- **POST** `/api/services/`: Create a new service
- **GET** `/api/services/<id>/`: Retrieve details of a specific service
- **PUT** `/api/services/<id>/`: Update a service
- **DELETE** `/api/services/<id>/`: Delete a service

#### Service Providers
- **GET** `/api/service-providers/`: List all service providers
- **POST** `/api/service-providers/`: Add a new service provider
- **GET** `/api/service-providers/<id>/`: Retrieve details of a specific service provider
- **PUT** `/api/service-providers/<id>/`: Update a service provider
- **DELETE** `/api/service-providers/<id>/`: Delete a service provider

#### Bookings
- **GET** `/api/bookings/`: List all bookings
- **POST** `/api/bookings/`: Create a new booking
- **GET** `/api/bookings/<id>/`: Retrieve details of a specific booking
- **PUT** `/api/bookings/<id>/`: Update a booking
- **DELETE** `/api/bookings/<id>/`: Cancel a booking

#### Customers
- **GET** `/api/customers/`: List all customers
- **POST** `/api/customers/`: Add a new customer
- **GET** `/api/customers/<id>/`: Retrieve details of a specific customer
- **PUT** `/api/customers/<id>/`: Update customer information
- **DELETE** `/api/customers/<id>/`: Remove a customer

   ```

### License

This project is licensed under the MIT License.


