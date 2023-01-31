from datetime import date

from pydantic import BaseModel, EmailStr, constr

from .enums import Gender
import app.config as config


class ConfirmationCode(BaseModel):
    code: str


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id: int | None
    email: EmailStr
    name: constr(max_length=config.USER_NAME_LENGTH)
    birthdate: date | None
    location: constr(max_length=config.USER_LOCATION_LENGTH) | None
    gender: Gender | None
    target_gender: Gender | None
    interests: list[constr(max_length=config.USER_INTEREST_LENGTH)]
    brief_description: constr(max_length=config.USER_BRIEF_DESCRIPTION_LENGTH) | None
    description: constr(max_length=config.USER_DESCRIPTION_LENGTH) | None
    creation_date: date

    class Config:
        orm_mode = True


class PasswordChangeRequest(BaseModel):
    new_password: str
