from fastapi import FastAPI

app = FastAPI()

from app.db import initialize_db, finalize_db
from app.redis import initialize_redis, finalize_redis


@app.on_event('startup')
async def on_start():
    await initialize_db()
    await initialize_redis()


@app.on_event('shutdown')
async def on_shutdown():
    await finalize_db()
    await finalize_redis()
