from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import (Column, Integer, String, Boolean)
from sqlalchemy.sql.expression import null
from src.base.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    projects = relationship("ProjectModel", back_populates="owner")
    jobs = relationship("JobModel", back_populates="task_owner")
