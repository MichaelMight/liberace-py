from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.exceptions import NotFoundException
from app.core.database import get_db
from app.utils.security import get_password_hash


class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def create_user(self, user_in: UserCreate) -> User:
        now = datetime.utcnow()
        user = User(
            username=user_in.username,
            hashed_password=get_password_hash(user_in.password),
            is_active=user_in.is_active,
            is_superuser=user_in.is_superuser,
            created_at=now,
            updated_at=now
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def update_user(self, user_id: int, user_in: UserUpdate) -> User:
        user = await self.get_user(user_id)
        update_data = user_in.dict(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        update_data["updated_at"] = datetime.utcnow()

        for field, value in update_data.items():
            setattr(user, field, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise NotFoundException(f"User with id {user_id} not found")
        return user