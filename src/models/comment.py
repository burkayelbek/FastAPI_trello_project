from src.base.database import Base
from sqlalchemy import (Column, Date, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship


class CommentModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True,nullable=False, index=True)
    description = Column(String, nullable=False)
    date_posted = Column(Date)
    comment_id = Column(Integer, ForeignKey("jobs.id"))
    comment = relationship("JobModel", back_populates="comments", foreign_keys=[comment_id])
