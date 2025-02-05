import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import auth, users, tasks
from database.session import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully")

    yield
    
    # Shutdown
    await engine.dispose()
    print("Database connection closed")

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
