from app.repositories import user_repository
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db, email, password):

    hashed = hash_password(password)

    return user_repository.create_user(db, email, hashed)


def login_user(db, email, password):

    user = user_repository.get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"user_id": user.id})

    return token