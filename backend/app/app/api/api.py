from fastapi import APIRouter

from app.api.routers import auth, books, plans, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
