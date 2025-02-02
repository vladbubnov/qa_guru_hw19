import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BROWSERSTACK_URL: str
    USER_NAME: str
    ACCESS_KEY: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')


settings = Settings()
