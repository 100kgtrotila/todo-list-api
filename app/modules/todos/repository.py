from sqlalchemy.orm import Session

from app.modules.todos.models import Todo


class TodoRepository:
    def get_todo_by_title(self, db: Session, title:str):
        return db.query(Todo).filter(Todo.title == title).first()

    def create_todo(self, db: Session, title: str, description: str, user_id: int):
        db_todo = Todo(
            title=title,
            description=description,
            owner_id=user_id
        )

        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def get_todos_by_user(self, db: Session, user_id: int):
        return db.query(Todo).filter(Todo.owner_id == user_id).all()