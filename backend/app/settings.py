from enum import Enum

from pydantic import BaseSettings


class AppEnvironment(str, Enum):
    DEBUG = 'DEBUG'
    DEVELOPMENT = 'DEVELOPMENT'
    PRODUCTION = 'PRODUCTION'


class AppSettings(BaseSettings):
    environment = AppEnvironment.DEVELOPMENT
    redis_url: str
    database_url: str
    
    class Config:
        secrets_dir = '/run/secrets'
