from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    first_name: str | None
    last_name: str | None
    phone: str | None

    class Config:
        from_attributes = True