from enum import Enum
from datetime import date

from pydantic import BaseModel, EmailStr


class ErrorResponse(BaseModel):
    code: int
    description: str


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
