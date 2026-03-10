from app.repositories import todo_repository

def create_todo(db, todo, user_id):

    return todo_repository.create_todo(db, todo, user_id)


def get_todos(db, user_id):

    return todo_repository.get_todos(db, user_id)


def complete_todo(db, todo_id, user_id):

    return todo_repository.complete_todo(db, todo_id, user_id)