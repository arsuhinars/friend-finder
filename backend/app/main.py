from fastapi import FastAPI

app = FastAPI()


# Include API routers
from .routers import router

app.include_router(router)
