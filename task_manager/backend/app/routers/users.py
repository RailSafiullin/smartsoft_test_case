from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from crud.user import user_crud
from schemas.user import UserCreate, User, UserUpdate
from models.user import User
from dependencies import get_current_user

router = APIRouter(tags=["users"])

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    existing_user = await user_crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await user_crud.create_user(db, user.model_dump())

@router.get("/users/me", response_model=User)
async def read_user_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.put("/users/me", response_model=User)
async def update_user_me(
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_user = await user_crud.update_user(db, current_user.id, user_update.model_dump(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_me(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted_user = await user_crud.delete_user(db, current_user.id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return None