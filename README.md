# FastAPI Shorten Link

A simple URL shortener project built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic**. The project includes Docker Compose support for running the API, database, and pgAdmin together.

## Requirements

### Recommended: Docker Setup

- Docker
- Docker Compose

### Local Python Setup

- Python 3.13+
- PostgreSQL 17+ or another compatible PostgreSQL server
- `pip`
- `virtualenv` or Python `venv`

## Project Stack

- **FastAPI** for the web API
- **Uvicorn** as the ASGI server
- **PostgreSQL** as the database
- **SQLAlchemy** for database access
- **Alembic** for database migrations
- **pgAdmin** for database management in Docker Compose

## Installation With Docker Compose

This is the easiest way to run the project because PostgreSQL and pgAdmin are included.

### 1. Clone The Repository

```bash
git clone https://github.com/Erfun-H/fastapi-shorten-link.git
cd fastapi-shorten-link
```

### 2. Create Environment File

The project already includes `.env.example`. Copy it to `.env.dev` if needed:

```bash
cp .env.example .env.dev
```

Default development values:

```env
APP_ENV=development
DEBUG=true

POSTGRES_USER=example_user
POSTGRES_DB=example_db
POSTGRES_PASSWORD=example_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

SECRET_KEY=secret_key

PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=1234
```

### 3. Build And Start Services

```bash
docker compose up --build
```

The services will start at:

- API: `http://localhost:8000`
- FastAPI docs: `http://localhost:8000/docs`
- pgAdmin: `http://localhost:5050`

### 4. Apply migrations

```bash
docker compose exec app alembic upgrade head
```


### 4. Stop Services

```bash
docker compose down
```

To remove the database volume too:

```bash
docker compose down -v
```

## Local Installation Without Docker

Use this option if you want to run FastAPI directly on your machine.

### 1. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a local environment file:

```bash
cp .env.example .env.dev
```

For local PostgreSQL, update `POSTGRES_HOST` from `db` to `localhost`:

```env
POSTGRES_HOST=localhost
```

Make sure your PostgreSQL database, user, and password match the values in `.env.dev`.

### 4. Load Environment Variables

```bash
export $(grep -v '^#' .env.dev | xargs)
```

On Windows PowerShell, set the variables manually or use a dotenv-compatible tool.

### 5. Run The API

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Open:

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

## Database Migrations

Alembic is configured for database migrations.

Create a new migration:

```bash
alembic revision --autogenerate -m "your migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback one migration:

```bash
alembic downgrade -1
```

When using Docker Compose, run Alembic commands inside the app container:

```bash
docker compose exec app alembic upgrade head
```

## Useful Commands

```bash
# Start all Docker services
docker compose up --build

# Start in background
docker compose up -d --build

# View logs
docker compose logs -f app

# Open app container shell
docker compose exec app bash

# Stop services
docker compose down
```

## Environment Variables

| Variable | Description | Example |
| --- | --- | --- |
| `APP_ENV` | Application environment | `development` |
| `DEBUG` | Enables FastAPI debug mode | `true` |
| `POSTGRES_USER` | PostgreSQL username | `example_user` |
| `POSTGRES_DB` | PostgreSQL database name | `example_db` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `example_password` |
| `POSTGRES_HOST` | PostgreSQL host | `db` or `localhost` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` |
| `SECRET_KEY` | Application secret key | `secret_key` |
| `PGADMIN_DEFAULT_EMAIL` | pgAdmin login email | `admin@gmail.com` |
| `PGADMIN_DEFAULT_PASSWORD` | pgAdmin login password | `1234` |

## Project Structure

```text
.
├── alembic/              # Alembic migration configuration
├── src/
│   ├── core/             # Core database configuration
│   ├── shortener/        # Shortener application package
│   └── main.py           # FastAPI application entry point
├── .env.example          # Example environment variables
├── compose.yaml          # Docker Compose services
├── Dockerfile            # API container image
├── requirements.txt      # Python dependencies
└── README.md
```

## Notes

- Do not use default passwords in production.
- Change `SECRET_KEY` before deploying.
- Use `.env.prod` or your deployment platform secrets for production configuration.
