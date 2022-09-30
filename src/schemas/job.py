from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum


class Status(int, Enum):
    RECEIVED = 1
    STARTED = 2
    IN_PROGRESS = 3
    DONE = 4


class JobBase(BaseModel):
    title: str
    description: str
    status: Optional[int] = 1


class JobCreate(JobBase):
    date_start: Optional[date] = None
    date_finish: Optional[date] = None


class JobOut(JobBase):
    id: int
    title: str
    created_at: date
    status: int
    description: Optional[str] = None
    date_start: Optional[date] = None
    date_finish: Optional[date] = None
    date_completed: Optional[date] = None

    class Config:
        orm_mode = True


class JobUpdate(JobBase):
    date_start: Optional[date]
    date_finish: Optional[date]
    status: Optional[int] = 1
