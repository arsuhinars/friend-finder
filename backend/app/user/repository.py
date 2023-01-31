from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def get_user_by_id(session: AsyncSession, id: int):
    result = await session.execute(select(User).where(User.id == id))
    return result.scalar_one_or_none()


async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def save_user(session: AsyncSession, user: User):
    session.add(user)
    return user
