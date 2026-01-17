from os import access

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.auth.schemas import UserCreate
from app.modules.auth.repository import UserRepository
from app.core.security import get_password_hash, verify_password, create_access_token


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

    def login_user(self, db: Session, password: str, user_email: str):
        user = self.repository.get_user_by_email(db, user_email)

        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(data = {"sub": str(user.id)})
        return {"access_token": access_token,
                "token_type": "bearer"}



