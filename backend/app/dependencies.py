from redis.asyncio import Redis

from .main import app


async def get_redis_client() -> Redis:
    try:
        redis = Redis(connection_pool=app.state.redis_pool)
        yield redis
    finally:
        await redis.close()
