from redis.asyncio import Redis

from app.settings import AppSettings


@lru_cache
def get_settings():
    return AppSettings()


async def get_redis_client() -> Redis:
    try:
        redis = Redis(connection_pool=app.state.redis_pool)
        yield redis
    finally:
        await redis.close()
