from src.models.user import UserModel
from src.schemas.user import UserCreate
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # For Hashing Password
from src.models.user import UserModel
from sqlalchemy import or_

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_new_user(user: UserCreate, db: Session):
    new_user = UserModel(
        username=user.username,
        hashed_password=_hash_password(user.password),
        email=user.email,
        is_active=True,
        is_superuser=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(username: str, db: Session):
    user = db.query(UserModel).filter(or_(UserModel.username == username,  UserModel.email == username)).first()
    return user


def _hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
