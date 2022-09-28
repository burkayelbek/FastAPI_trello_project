from src.base.database import Base
from sqlalchemy import (Column, Integer, String, Boolean, Date, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text


class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    created_at = Column(Date)
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("UserModel", back_populates="projects", foreign_keys=[owner_id])
    jobs = relationship("JobModel", back_populates="project")
