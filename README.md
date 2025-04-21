# LiteStar Web Service

This project is a Python web service built using LiteStar and Advanced-SQLAlchemy, designed for user management with a PostgreSQL database.

## Project Structure

```
litar-web-service
├── app
│   ├── controllers
│   │   └── user_controller.py  # Controllers for handling requests
│   ├── models
│   │   └── user.py             # SQLAlchemy models
│   ├── schemas
│   │   └── user.py             # Msgspec schemas for validation and serialization
│   ├── services
│   │   └── user_service.py     # Business logic for database operations
│   ├── db
│   │   ├── __init__.py         # Database initialization
│   │   └── base.py             # Base SQLAlchemy configuration
│   ├── __init__.py             # Application initialization
│   └── main.py                 # Application entry point
├── migrations
│   ├── env.py                  # Alembic configuration
│   ├── versions                # Folder for migration versions
│   └── alembic.ini             # Alembic settings
├── config.py                   # Application configuration
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Dockerfile for building the application
├── pyproject.toml              # Poetry configuration
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies (if not using Poetry)
```

## Features

- **User Management**: Create, retrieve, update, and delete users.
- **PostgreSQL Database**: Utilizes PostgreSQL for data storage.
- **Advanced-SQLAlchemy**: Manages database interactions.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alexpantyukhin/user_crud
   cd user_crud
   ```

2. **Run Docker Compose**:
   Make sure Docker is installed and running on your system. Then, execute the following command to start the application and its dependencies:
   ```bash
   docker-compose up --build
   ```

   This will build the Docker images, start the PostgreSQL database, apply migrations, and run the application.

## Usage

- **Create User**: Send a POST request to `/users` with user details.
- **Get All Users**: Send a GET request to `/users`.
- **Get User**: Send a GET request to `/users/{id}`.
- **Update User**: Send a PUT request to `/users/{id}` with updated details.
- **Delete User**: Send a DELETE request to `/users/{id}`.

## License

This project is licensed under the MIT License.
