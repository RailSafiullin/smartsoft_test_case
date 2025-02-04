from datetime import datetime
from pydantic import BaseModel
from schemas.user import User

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "open"

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    owner_id: int
    owner: User

    class Config:
        from_attributes = True