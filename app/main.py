from fastapi import FastAPI

from app.modules.auth.routes import router as auth_router
from app.modules.todos.routes import router as todos_router

app = FastAPI(title="Todo List API")

app.include_router(auth_router)
app.include_router(todos_router)


@app.get("/")
def root():
    return {"message": "Welcome to Todo List API"}