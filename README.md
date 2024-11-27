# FastAPI Project Template

A production-ready FastAPI project template that helps you kickstart your Python web application with best practices.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-green.svg)](https://fastapi.tiangolo.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🚀 Modern Python with FastAPI and async support
- 📦 Dependency management with Poetry
- 🏗️ Clean architecture with clear separation of concerns
- 🔒 Built-in error handling and type checking
- 🔄 HTTP client with retry mechanism
- ⚡ Ready-to-use project structure
- 🧪 Testing setup with pytest
- 📝 Type hints throughout the codebase
- 🗄️ Database support for both SQLite and PostgreSQL
- 🔍 Comprehensive logging system
- 📊 Domain-driven design patterns

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/): Modern web framework
- [Pydantic](https://docs.pydantic.dev/) V2: Data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) 2.0: ORM
- [HTTPX](https://www.python-httpx.org/): Async HTTP client
- [Poetry](https://python-poetry.org/): Dependency management
- [Pytest](https://docs.pytest.org/): Testing framework
- [Alembic](https://alembic.sqlalchemy.org/): Database migrations

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Poetry

### Installation

1. Create a new project using this template:
```bash
git clone https://github.com/MichaelMight/fliberace-py my-project
cd my-project
```

2. Install dependencies:
```bash
poetry install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Configure database (SQLite by default):
```env
# Use SQLite (default)
DATABASE_TYPE=sqlite

# Or use PostgreSQL
# DATABASE_TYPE=postgresql
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

5. Run the development server:
```bash
poetry run uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to see the API documentation.

## 📁 Project Structure

```
project_name/
├── pyproject.toml          # Dependencies and project metadata
├── README.md              # Project documentation
├── .env                   # Environment variables
├── .github/              # GitHub Actions workflows
├── app/
│   ├── api/              # API routes
│   │   └── v1/
│   │       └── endpoints/
│   ├── core/             # Core configuration
│   │   ├── config.py     # Application configuration
│   │   └── exceptions.py # Global exception handlers
│   ├── models/           # Database models
│   │   ├── base.py      # Base model class
│   │   └── domain/      # Domain models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   └── utils/            # Utility functions
│       ├── http.py      # HTTP client with retry
│       └── logger.py    # Logging configuration
├── main.py               # Application entry point
└── tests/               # Test suite
```

## 🧪 Testing

Run tests with pytest:
```bash
poetry run pytest
```

For coverage report:
```bash
poetry run pytest --cov=app tests/
```

## 📝 Example Usage

The template comes with a complete user management implementation as an example:

```python
# app/api/v1/endpoints/user.py
from fastapi import APIRouter, Depends, status
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserInDB
from app.utils.logger import logger

router = APIRouter()

@router.post("/users", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    service: UserService = Depends(UserService)
) -> UserInDB:
    """
    Create new user with:
    - Username validation
    - Password hashing
    - Automatic timestamp handling
    - Database persistence
    """
    logger.info(f"Creating new user with username: {user_in.username}")
    return await service.create_user(user_in)
```

This example demonstrates key features of the template:
- FastAPI dependency injection
- Pydantic schemas for request/response validation
- Service layer for business logic
- Structured logging
- Clean architecture patterns
- Type hints and documentation

To see the complete implementation, check:
- `app/models/user.py` - SQLAlchemy model
- `app/schemas/user.py` - Pydantic schemas
- `app/services/user_service.py` - Business logic
- `tests/test_user.py` - Unit tests

## 🔧 Configuration

The template supports various configuration options through environment variables:

```env
# Application
APP_NAME=FastAPI Project
DEBUG=True

# Database
DATABASE_TYPE=sqlite  # or postgresql
DATABASE_URL=        # required for postgresql

# Logging
LOG_LEVEL=INFO

# API
API_V1_STR=/api/v1
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html)

## 📬 Contact

X: [@cx_pageup](https://x.com/cx_pageup)

Project Link: [fliberace-py](https://github.com/MichaelMight/liberace-py)

