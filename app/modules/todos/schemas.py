from typing import Optional

from pydantic import BaseModel, ConfigDict


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class CreateTodo(TodoBase):
    pass

class UpdateTodo(TodoBase):
    title = Optional[str]
    description: Optional[str] = None

class TodoResponse(TodoBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
