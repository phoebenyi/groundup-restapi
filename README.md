# Log Analysis REST API

This project implements a simple REST API that processes log data from a CSV file and returns a report summary of the logs in M6.csv.

## Prerequisites

- Docker
- Docker Compose

## Setup and Deployment

1. Clone this repository (or unzip the project files) into a directory.
2. Navigate to the project directory.
3. Run the following command to build and start the Docker containers:

   ```
   docker-compose up --build
   ```

   The API will be accessible at `http://localhost:10000`.

## Usage

To use the API, send a POST request to the `/generateReport` endpoint with a CSV file.

## API Response

The API returns a JSON response with the following statistics for each numerical feature:

- Minimum value
- Maximum value
- Mean
- Standard Deviation
- Kurtosis

## Methodology

1. Built using FastAPI for high-performance API development.
2. Processes uploaded CSV files using pandas.
3. Calculates required statistics for all numerical columns.
4. Returns results as a JSON response.
5. Containerized with Docker for consistent deployment across environments.