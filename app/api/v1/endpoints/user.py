from fastapi import APIRouter, Depends, status
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.services.user_service import UserService

router = APIRouter()


@router.post("/users", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_in: UserCreate,
        service: UserService = Depends(UserService)
) -> UserInDB:
    """Create new user"""
    return await service.create_user(user_in)


@router.get("/users/{user_id}", response_model=UserInDB)
async def get_user(
        user_id: int,
        service: UserService = Depends(UserService)
) -> UserInDB:
    """Get user by ID"""
    return await service.get_user(user_id)


@router.put("/users/{user_id}", response_model=UserInDB)
async def update_user(
        user_id: int,
        user_in: UserUpdate,
        service: UserService = Depends(UserService)
) -> UserInDB:
    """Update user"""
    return await service.update_user(user_id, user_in)
