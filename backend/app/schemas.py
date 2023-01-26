from enum import Enum
from datetime import date

from pydantic import BaseModel, EmailStr


class ErrorResponse(BaseModel):
    code: int
    description: str


class AuthRequest(BaseModel):
    login: str
    password: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class ConfirmationCode(BaseModel):
    code: str


class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'


class UserProfile(BaseModel):
    id: int | None
    name: str
    birthdate: date | None
    location: str | None
    gender: Gender | None
    target_gender: Gender | None
    interests: list[str]
    short_description: str | None
    description: str | None


class PasswordChangeRequest(BaseModel):
    new_password: str


class ChatType(str, Enum):
    DIALOG = 'dialog'
    ANONYMOUS = 'anonymous'


class UserChat(BaseModel):
    id: int
    type: ChatType
    user_profile: UserProfile | None


class Message(BaseModel):
    id: int | None
    chat_id: int | None
    timestamp: int | None
    sender_id: int | None
    content: str


class UpdateEventType(str, Enum):
    NEW_LIKE = 'new_like'
    NEW_CHAT = 'new_chat'
    NEW_MESSAGE = 'new_message'
    CHAT_DELETED = 'chat_deleted'


class UpdateEvent(BaseModel):
    timestamp: int
    type: UpdateEventType
    profile: UserProfile | None
    chat: UserChat | None
    message: Message | None
    chat_id: int | None
