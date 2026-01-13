from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.auth.schemas import UserCreate
from app.modules.auth.repository import UserRepository
from app.core.security import get_password_hash

class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    def register_new_user(self, db: Session, user_data: UserCreate):
        exsisting_user = self.repository.get_user_by_email(db, email=user_data.email)
        if exsisting_user:
            raise  HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email alredy registered"
            )

        hashed_pwd = get_password_hash(user_data.password)

        new_user = self.repository.create_user(db, user_data, hashed_pwd)

        return new_user



