import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.base.settings import Settings
from typing import Generator
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

settings = Settings()
logger = logging.getLogger(__name__)


engine = settings.postgresql_database_connection()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
