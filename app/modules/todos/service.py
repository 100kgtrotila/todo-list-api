from sqlalchemy.orm import Session

from app.modules.todos.repository import TodoRepository
from app.modules.todos.schemas import CreateTodo


class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def create_new_task(self, db: Session, todo_data: CreateTodo, user_id: int):
            return self.repository.create_todo(db, todo_data, user_id)

    def get_my_tasks(self, db: Session, user_id: int):
        return self.repository.get_todos_by_user(db, user_id)