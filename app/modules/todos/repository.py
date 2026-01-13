from sqlalchemy.orm import Session

from app.modules.todos.models import Todo


class TodoRepository:
    def get_todo_by_title(self, db: Session, title:str):
        return db.query(Todo).filter(Todo.title == title).first()