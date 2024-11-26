from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from app.core.database import init_db
from app.utils.logger import logger
from app.api.v1.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing application...")
    init_db()
    logger.info("Application started successfully")
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

@app.get("/", 
    response_model=dict[str, str],
    status_code=status.HTTP_200_OK,
    tags=["health-check"],
    summary="Health Check",
    description="Returns the health status of the API"
)
async def health_check():
    return {"status": "healthy"}

# API routers
app.include_router(api_router, prefix="/api/v1")