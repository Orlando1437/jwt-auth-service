from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="JWT Auth Service",
    description="Service for authentication and authorization",
    version="1.0.0"
)

app.include_router(auth.router)

@app.get("/")
def root():
    return {
        "message": "JWT Auth Service funcionando"
    }
