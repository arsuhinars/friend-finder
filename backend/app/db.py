from sqlalchemy.orm import declarative_base, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_scoped_session
from sqlalchemy.ext.asyncio.session import async_sessionmaker, AsyncSession

from app.main import app
from app.dependencies import get_settings
from app.settings import AppEnvironment


Base: DeclarativeBase = declarative_base()


from app.user.models import *


async def initialize_db():
    app.state.db_engine = create_async_engine(
        get_settings().database_url,
        echo=(get_settings().environment == AppEnvironment.DEVELOPMENT)
    )
    app.state.db_session_maker = async_sessionmaker(
        app.state.db_engine,
        autoflush=False,
        expire_on_commit=False
    )

    Base.metadata.create_all(app.state.db_engine)


async def finalize_db():
    await app.state.db_engine.dispose()


def get_engine() -> AsyncEngine:
    return app.state.db_engine


def get_session_maker() -> async_sessionmaker:
    return app.state.db_session_maker
