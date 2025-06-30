# Late Show API Challenge

## Setup Instructions

### PostgreSQL

- Install PostgreSQL and ensure it is running.
- Create a database for the application.
- Note the database connection URL (e.g., `postgresql://user:password@localhost:5432/dbname`).

### Flask and Environment Variables

- Install Python 3.8+ and pip.
- Install dependencies using Pipenv or pip:

  ```bash
  pipenv install
  # or
  pip install -r requirements.txt
  ```

- Create a `.env` file in the project root with the following variables:
  
  DATABASE_URL=your_postgresql_database_url
  JWT_SECRET_KEY=your_jwt_secret_key

## How to Run

### Database Migration

- Run migrations to set up the database schema:

  ```bash
  flask db migrate
  flask db upgrade
  ```

  Or using the CLI:

  ```bash
  python manage.py db migrate
  python manage.py db upgrade
  ```

### Seeding the Database

- Seed the database with initial data:

  ```bash
  python -m server.seed

  ```

### Running the Application

- Run the Flask development server:

  ```bash
  flask run
  ```

  Or using the CLI:

  ```bash
  python manage.py run
  ```

## Authentication Flow

### Register

- Endpoint: `POST /register`
- Request body:

  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

- Response: User object on success.

### Login

- Endpoint: `POST /login`
- Request body:

  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

- Response: JSON Web Token (JWT) access token:

  ```json
  {
    "access_token": "your_jwt_token"
  }
  ```

### Token Usage

- Include the JWT token in the `Authorization` header for protected routes:

  Authorization: Bearer your_jwt_token

## Route List and Sample Requests/Responses

### Episodes

- `GET /episodes`
  - Response: List of episodes

  ```json
  [
    {
      "id": 1,
      "date": "2024-01-01",
      "number": 101
    },
    ...
  ]
  ```

- `GET /episodes/<id>`
  - Response: Single episode object
- `DELETE /episodes/<id>` (Protected)
  - Response:

  ```json
  {
    "msg": "Episode and related appearances deleted"
  }
  ```

### Appearances

- `POST /appearances` (Protected)
- Request body:

  ```json
  {
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
  }
  ```

- Response: Created appearance object

### Guests

- `GET /guests`
- Response: List of guests

  ```json
  [
    {
      "id": 1,
      "name": "Guest Name",
      "occupation": "Occupation"
    },
    ...
  ]
  ```

## Postman Usage Guide

- Import the Postman collection file located at:

  server/challenge-4-lateshow.postman_collection.json

- Use the collection to test all API endpoints.
- Set environment variables in Postman for the base URL and JWT token as needed.

## GitHub Repository

- [GitHub Repo Link](https://github.com/DunstanKiiru/late-show-api-challenge)  
