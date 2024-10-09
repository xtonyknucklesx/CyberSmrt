from fastapi import APIRouter, Depends
from app.schemas.auth_schema import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    # Placeholder implementation
    return {"access_token": "fake_token", "token_type": "bearer"}