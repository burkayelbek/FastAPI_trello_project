from src.base.database import Base
from sqlalchemy import (Boolean, Column, Date, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship


class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(Date)
    date_start = Column(Date)
    date_finish = Column(Date)
    date_completed = Column(Date)
    status = Column(Integer, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'))
    job_owner_id = Column(Integer, ForeignKey('users.id'))
    project = relationship("ProjectModel", back_populates="jobs", foreign_keys=[project_id])
    comments = relationship("CommentModel", back_populates="comment")
    task_owner = relationship("UserModel", back_populates="jobs", foreign_keys=[job_owner_id])
