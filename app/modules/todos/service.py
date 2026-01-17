from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.todos.repository import TodoRepository
from app.modules.todos.schemas import CreateTodo, UpdateTodo


class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def create_new_task(self, db: Session, todo_data: CreateTodo, user_id: int):
            return self.repository.create_todo(db, title=todo_data.title, description=todo_data.description, user_id=user_id)

    def get_my_tasks(self, db: Session, user_id: int):
        return self.repository.get_todos_by_user(db, user_id)

    def delete_task(self, db: Session, todo_id: int, user_id: int):
        success = self.repository.delete_todo(db, todo_id, user_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    def update_task(self, db: Session, todo_id: int, todo_data: UpdateTodo, user_id: int):
        update_dict = todo_data.model_dump(exclude_unset=True)
        updated_todo = self.repository.update_todo(db, update_dict, todo_id, user_id)
        if not updated_todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        return updated_todo