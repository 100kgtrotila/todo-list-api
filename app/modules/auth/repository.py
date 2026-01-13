from sqlalchemy.orm import Session

from app.modules.auth.models import User
from app.modules.auth.schemas import UserCreate


class UserRepository:
    def get_user_by_email(self, db: Session, email:str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, user_data: UserCreate, hashed_password:str):
        db_user = User(
            email=user_data.email,
            password=hashed_password,
            name=user_data.name
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)

        return db_user