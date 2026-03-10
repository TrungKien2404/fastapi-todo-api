from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    description = Column(String)

    is_done = Column(Boolean, default=False)

    due_date = Column(DateTime, nullable=True)

    tags = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey("users.id"))