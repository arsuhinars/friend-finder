from functools import lru_cache
from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

from app.settings import AppSettings
from app.redis import get_redis_pool
from app.db import get_session_maker


@lru_cache
def get_settings():
    return AppSettings()


async def get_db_session() -> AsyncIterable[AsyncSession]:
    session_maker = get_session_maker()
    with session_maker() as session:
        yield session


async def get_redis_client() -> AsyncIterable[Redis]:
    try:
        redis = Redis(connection_pool=get_redis_pool())
        yield redis
    finally:
        await redis.close()
