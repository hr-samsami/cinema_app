# FastAPI Cinema Application

A FastAPI application for managing a cinema, including room and movie management, seat booking, and admin CRUD operations.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Room Management**: Create, read, update, and delete rooms.
- **Movie Management**: Manage movies including scheduling and details.
- **Seat Booking**: Book and manage seats for different shows.
- **Admin API**: CRUD operations for administrative tasks.

## Technologies

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Async Support**: `asyncpg` for async PostgreSQL access
- **Testing**: Pytest with `httpx` for async testing
- **Docker**: Containerization for development and production

## Installation

### Prerequisites

Ensure you have [Python 3.11](https://www.python.org/downloads/) and [Docker](https://www.docker.com/products/docker-desktop) installed.

### Setting Up a Virtual Environment

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - **On macOS/Linux**:
      ```sh
      source .venv/bin/activate
      ```
    - **On Windows**:
      ```sh
      .venv\Scripts\activate
      ```

4. Install dependencies:

    ```sh
    pip install -r requirements/dev.txt
    ```

### Adding New Packages

When adding new packages, follow these steps:

1. Add the new package to the appropriate `requirements/base.in` file.

2. Run the following command to update `requirements/base.txt` and `requirements/dev.txt`:

    ```sh
    pip-compile --strip-extras requirements/base.in
    ```

## Usage

### Running Locally

1. Ensure your database is running and accessible.

2. Start the FastAPI application:

    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

3. Open your browser and navigate to `http://localhost:8000` to access the API. The interactive documentation can be found at `http://localhost:8000/docs`.

### Running with Docker

1. Build the Docker image:

    ```sh
    sudo docker build -t cinema -f ./dockerfiles/Dockerfile.dev .
    ```

2. Run the Docker container:

    ```sh
    sudo docker run -d -p 8000:8000 --name cinema_container cinema
    ```

3. Access the API at `http://localhost:8000`.

## Testing

### Running Tests

1. Ensure your virtual environment is activated.

2. Run the tests:

    ```sh
    pytest
    ```

## Docker

The Dockerfile located at `dockerfiles/Dockerfile.dev` can be used to build and run the application in a containerized environment. For more details, see the [Docker](#docker) section.


export PYTHONPATH=$(pwd)
uvicorn main:app --reload
