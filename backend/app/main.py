from fastapi import FastAPI
from app.routes import auth_routes, user_routes

app = FastAPI()

# Include routes
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}