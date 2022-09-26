from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from src.base.settings import Settings
import logging

Base = declarative_base()

settings = Settings()
logger = logging.getLogger(__name__)


class DatabaseManagement:

    def __init__(self):
        self.engine = settings.postgresql_database_connection()
        self.database_session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.base = Base
        self.base.query = self.database_session.query_property()
        # For use scoped session, to see automatically all models

    def __enter__(self):
        """
        This Method Provides Database Connection Process Before Requests
        :return:
        """
        self.database_session.connection()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This Method Provides Database Connection Close Process After Requests
        :return:
        """
        self.database_session.close()

    def postgresql_create_tables(self) -> bool:
        """
        This Method Creates Necessary Postgresql Models For Platform Integration.
        :return:
        """
        try:
            self.base.metadata.create_all(self.engine)

            return True
        except Exception as error:
            logger.error(msg=error)
            return False
