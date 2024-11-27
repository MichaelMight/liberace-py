from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool
from .config import get_settings

settings = get_settings()

# SQLite configuration
if settings.DATABASE_TYPE == "sqlite":
    engine = create_engine(
        settings.sqlalchemy_database_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool  # add this to test SQLite
    )
else:
    engine = create_engine(settings.sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()