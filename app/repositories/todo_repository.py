from sqlalchemy.orm import Session
from app.models.todo import Todo

def create_todo(db: Session, todo, user_id):

    new_todo = Todo(**todo.dict(), owner_id=user_id)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


def get_todos(db: Session, user_id):

    return db.query(Todo).filter(Todo.owner_id == user_id).all()


def complete_todo(db: Session, todo_id, user_id):

    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.owner_id == user_id
    ).first()

    if todo:
        todo.is_done = True
        db.commit()
        db.refresh(todo)

    return todo