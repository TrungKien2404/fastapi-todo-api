from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import todo_router, auth_router
from app.models import user, todo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Todo API")

@app.get("/")
def root():
    return {"message": "Welcome"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(todo_router.router)
app.include_router(auth_router.router)