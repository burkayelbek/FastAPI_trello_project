from pydantic import BaseModel
from datetime import date


class ProjectCreate(BaseModel):
    title: str


class ShowProject(BaseModel):
    id: int
    title: str
    is_active: bool
    created_at: date

    class Config:
        orm_mode = True


class ProjectUpdate(BaseModel):
    title: str
    is_active: bool
