
# Exxact Robotics - Backend Developer Test 

This repository contains a Django REST API for managing installations data, built for the Exxact Robotics technical backend test.

The API provides endpoints to list, filter, retrieve, update, and delete installations. The application also includes API documentation and is configured for code quality checks (isort, black, flake8) with CI.

---

## Features

- Django REST Framework
- SQLite database
- Filter support (`codepostal`, `statutseveso`, `etatactivite`)
- API documentation with Swagger (drf-spectacular)
- CI-ready with linting (isort, black, flake8)

---

## Requirements

- Python 3.11+
- pip
- virtualenv (recommended)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/elie-sokhon/exxact_robotics
```

---

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
```

#### On Linux/macOS:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply database migrations

```bash
cd backend
python manage.py migrate
```

---

### 5. Load installations data

If you have the GeoJSON dataset:

```bash
python manage.py load_installations /data/etablissements_icpe_pays_loire.geojson
```

---

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at:  
`http://127.0.0.1:8000/api/installations/`

API documentation (Swagger UI) at:  
`http://127.0.0.1:8000/api/schema/swagger-ui/`

---

## CI Configuration

This project uses GitHub Actions to automatically run:

- Code linting (isort, black, flake8)
- Django migrations check

---

## API Endpoints Summary

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/installations/` | List all installations |
| GET | `/api/installations/?codepostal=XXXXX` | Filter by postal code |
| GET | `/api/installations/?statutseveso=XXX` | Filter by SEVESO status |
| GET | `/api/installations/?etatactivite=XXX` | Filter by activity state |
| GET | `/api/installations/<gid>/` | Retrieve one installation |
| PATCH | `/api/installations/<gid>/` | Partial update |
| PUT | `/api/installations/<gid>/` | Full update |
| DELETE | `/api/installations/<gid>/` | Delete |

---

## Notes

- Default DB is SQLite for simplicity, easily configurable to PostgreSQL.
- See `core/settings.py` for customization.
- Swagger documentation powered by `drf-spectacular`.

---

## Author

Elie El Sokhon


