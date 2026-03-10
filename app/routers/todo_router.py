from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.todo_schema import TodoCreate
from app.services import todo_service
from app.core.database import get_db
from app.core.security import get_current_user
router = APIRouter(prefix="/api/v1/todos")


@router.post("/")
def create(todo: TodoCreate, db: Session = Depends(get_db)):

    user_id = 1

    return todo_service.create_todo(db, todo, user_id)


@router.get("/")
def list_todos(db: Session = Depends(get_db)):

    user_id = 1

    return todo_service.get_todos(db, user_id)


# @router.post("/{todo_id}/complete")
# def complete(todo_id: int, db: Session = Depends(get_db)):

#     user_id = 1

#     return todo_service.complete_todo(db, todo_id, user_id)
@router.post("/todos")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return todo_service.create_todo(db, todo, current_user.id)