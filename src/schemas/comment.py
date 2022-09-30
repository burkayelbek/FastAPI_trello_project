from pydantic import BaseModel
from datetime import date


class CommentCreate(BaseModel):
    description: str


class CommentOut(BaseModel):
    id: int
    description: str
    created_at: date

    class Config:
        orm_mode = True


class CommentUpdate(BaseModel):
    description: str
