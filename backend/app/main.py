import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Debugging
print("Database URL:", os.getenv("DATABASE_URL"))
print("Redis URL:", os.getenv("REDIS_URL"))

# Include routers (ensure your `users.py` has a `router` object)
from app.routes import users

app.include_router(users.router, prefix="/users", tags=["Users"])
