from pydantic import BaseModel, Field
from datetime import datetime

class TodoCreate(BaseModel):

    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    due_date: datetime | None = None
    tags: str | None = None


class TodoUpdate(BaseModel):

    title: str | None = None
    description: str | None = None
    is_done: bool | None = None