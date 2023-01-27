from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_url: str
    database_url: str
    
    class Config:
        secrets_dir = '/run/secrets'


settings = Settings()
