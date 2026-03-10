from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, email, hashed_password):

    user = User(email=email, hashed_password=hashed_password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email):

    return db.query(User).filter(User.email == email).first()