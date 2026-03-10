from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserLogin
from app.services import auth_service
from app.core.database import get_db

router = APIRouter(prefix="/api/v1/auth")

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    return auth_service.register_user(db, user.email, user.password)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    token = auth_service.login_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"access_token": token}