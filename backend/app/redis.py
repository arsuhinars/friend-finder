import redis.asyncio as redis

from app.main import app
from app.dependencies import get_settings

async def initialize_redis():
    app.state.redis_pool = redis.ConnectionPool.from_url(
        get_settings().redis_url
    )


async def finalize_redis():
    await app.state.redis_pool.disconnect()


def get_redis_pool() -> redis.ConnectionPool:
    return app.state.redis_pool
