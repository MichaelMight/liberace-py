from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from app.utils.security import verify_password


class UserRole(str, Enum):
    REGULAR = "regular"
    ADMIN = "admin"
    SUPERUSER = "superuser"


class UserDomain(BaseModel):
    id: int
    username: str
    is_active: bool
    role: UserRole
    last_login: Optional[datetime] = None
    login_attempts: int = 0

    @property
    def is_locked(self) -> bool:
        return self.login_attempts >= 3

    def record_login_attempt(self, success: bool) -> None:
        if success:
            self.login_attempts = 0
            self.last_login = datetime.utcnow()
        else:
            self.login_attempts += 1

    def can_access_admin_panel(self) -> bool:
        return self.role in [UserRole.ADMIN, UserRole.SUPERUSER] and self.is_active


