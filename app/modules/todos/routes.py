from typing import List

from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.models import User
from app.modules.todos.schemas import TodoResponse, CreateTodo, UpdateTodo
from app.modules.todos.service import TodoService

router = APIRouter(prefix="/todos", tags=["Todos"])

todos_service = TodoService()

@router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: CreateTodo, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return todos_service.create_new_task(db=db, todo_data=todo_data, user_id=current_user.id)

@router.get("/", response_model=List[TodoResponse])
def get_all_todos_by_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return todos_service.get_my_tasks(db=db, user_id=current_user.id)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db) , current_user: User = Depends(get_current_user)):
    todos_service.delete_task(db=db, todo_id=todo_id, user_id=current_user.id)
    return None
@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_data: UpdateTodo, db: Session = Depends(get_db) , current_user: User = Depends(get_current_user)):
    return todos_service.update_task(db=db, todo_id=todo_id, todo_data=todo_data, user_id=current_user.id)