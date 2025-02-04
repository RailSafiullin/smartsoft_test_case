from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from core.security import get_password_hash

class UserCRUD:
    async def get_user(self, db: AsyncSession, user_id: int):
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_user_by_email(self, db: AsyncSession, email: str):
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()

    async def create_user(self, db: AsyncSession, user_data: dict):
        hashed_password = get_password_hash(user_data["password"])
        db_user = User(
            username=user_data["username"],
            email=user_data["email"],
            hashed_password=hashed_password
        )
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

    async def update_user(self, db: AsyncSession, user_id: int, update_data: dict):
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(**update_data)
            .returning(User)
        )
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one_or_none()

    async def delete_user(self, db: AsyncSession, user_id: int):
        stmt = delete(User).where(User.id == user_id).returning(User)
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one_or_none()

user_crud = UserCRUD()