from fastapi import FastAPI
import redis.asyncio as redis

from .settings import settings

app = FastAPI()

@app.on_event('startup')
async def on_start():
    app.state.redis_pool = redis.ConnectionPool.from_url(settings.redis_url)


@app.on_event('shutdown')
async def on_shutdown():
    await app.state.redis_pool.disconnect()


# Include API routers
from .routers import router

app.include_router(router)
