from src.models.user import UserModel
from src.schemas.user import UserCreate
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # For Hashing Password


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


def _hash_password(password):
    return pwd_context.hash(password)
