from fastapi import FastAPI
from db.db import create_tables
from routers import users, auth, protected

app = FastAPI(title="RBAC with FastAPI")

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(protected.router)

@app.on_event("startup")
async def startup():
    await create_tables()

@app.get("/")
def home():
    return {"message": "Welcome to RBAC with FastAPI"}
