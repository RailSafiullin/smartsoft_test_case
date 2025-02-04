from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.task import Task
from datetime import datetime

class TaskCRUD:
    async def get_task(self, db: AsyncSession, task_id: int):
        result = await db.execute(select(Task).filter(Task.id == task_id))
        return result.scalar_one_or_none()

    async def get_user_tasks(self, db: AsyncSession, user_id: int, 
                            title: str = None, created_after: datetime = None):
        query = select(Task).filter(Task.owner_id == user_id)
        
        if title:
            query = query.filter(Task.title.contains(title))
        if created_after:
            query = query.filter(Task.created_at >= created_after)
            
        result = await db.execute(query)
        return result.scalars().all()

    async def create_task(self, db: AsyncSession, task_data: dict, user_id: int):
        db_task = Task(**task_data, owner_id=user_id)
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)
        return db_task

    async def update_task(self, db: AsyncSession, task_id: int, update_data: dict):
        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(**update_data)
            .returning(Task)
        )
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one_or_none()

    async def delete_task(self, db: AsyncSession, task_id: int):
        stmt = delete(Task).where(Task.id == task_id).returning(Task)
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one_or_none()

task_crud = TaskCRUD()