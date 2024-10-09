from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(request: UserCreate):
    # Placeholder implementation
    return {"id": 1, "username": request.username, "email": request.email}