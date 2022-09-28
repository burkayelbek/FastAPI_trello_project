from src.service.user import create_new_user
from src.base.database import get_db
from fastapi import APIRouter
from fastapi import Depends
from src.schemas.user import UserOut
from src.schemas.user import UserCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter


router = APIRouter()

@router.post("/create", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
