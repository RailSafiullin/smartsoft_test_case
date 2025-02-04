import uvicorn
from fastapi import FastAPI
from routers import auth, users, tasks
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
