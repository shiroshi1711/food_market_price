# Food Price Pipeline

A small automated data pipeline that fetches daily food commodity price data from the Indonesian Ministry of Trade's SP2KP API, transforms the data, and stores it in PostgreSQL.

## Pipeline

API → Python → Transform → PostgreSQL (Supabase)

The pipeline is containerized with Docker and automatically runs once a day using GitHub Actions.

## Features

- Fetches food price data from the SP2KP API
- Fetches the previous day's data
- Transforms API responses into a structured dataset
- Stores data in PostgreSQL
- Uses an upsert strategy to prevent duplicate records
- Uses Docker for a consistent runtime environment
- Runs automatically with GitHub Actions
- Uses environment variables and GitHub Secrets for configuration

## Project Structure

```text
foodprices/
├── .github/
│   └── workflows/
│       └── daily-fetch.yml
├── main.py
├── fetch.py
├── transform.py
├── database.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Database

The data is stored in a PostgreSQL table named `food_prices`.

Each price observation is uniquely identified by:

- `variant_id`
- `date`
- `region`

The pipeline uses PostgreSQL `ON CONFLICT DO UPDATE` so repeated runs do not create duplicate records.

## Configuration

Sensitive configuration is stored in environment variables.

For local development, create a `.env` file containing the required API and database configuration.

For GitHub Actions, the same values are stored as GitHub Secrets.

The `.env` file is not committed to the repository.

## Running Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the pipeline:

```bash
python main.py
```

The project can also be run using Docker Compose:

```bash
docker compose up --build
```

## Automation

GitHub Actions runs the pipeline once per day.

The workflow:

1. Checks out the repository
2. Builds the Docker image
3. Runs the pipeline container
4. Fetches the previous day's price data
5. Stores the processed data in PostgreSQL

## Data Source

Data is obtained from the Sistem Pemantauan Pasar dan Kebutuhan Pokok (SP2KP), Kementerian Perdagangan Republik Indonesia.

## Disclaimer

This project is for learning and data engineering purposes. The data is provided by the original source and may be subject to changes in availability, update timing, or accuracy.

## Author

Novia F Malia