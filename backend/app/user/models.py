from datetime import date

from sqlalchemy import func
from sqlalchemy import String, LargeBinary, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
import app.config as config
from .enums import Gender


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_key: Mapped[bytes] = mapped_column(
        LargeBinary(config.USER_PASSWORD_KEY_LENGTH)
    )
    password_salt: Mapped[bytes] = mapped_column(
        LargeBinary(config.USER_PASSWORD_SALT_LENGTH)
    )
    creation_date: Mapped(date) = mapped_column(server_default=func.now)
    name: Mapped[str] = mapped_column(String(config.USER_NAME_LENGTH))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_confirmed: Mapped[bool] = mapped_column(default=False)
    birthdate: Mapped[date | None]
    location: Mapped[str | None] = mapped_column(
        String(config.USER_LOCATION_LENGTH)
    )
    gender: Mapped[Gender | None]
    target_gender: Mapped[Gender | None]
    interests: Mapped[list(str) | None] = mapped_column(
        ARRAY(String(config.USER_INTEREST_LENGTH))
    )
    brief_description: Mapped[str | None] = mapped_column(
        String(config.USER_BRIEF_DESCRIPTION_LENGTH)
    )
    description: Mapped[str | None] = mapped_column(
        String(config.USER_DESCRIPTION_LENGTH)
    )
