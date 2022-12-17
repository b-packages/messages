from functools import lru_cache
from pydantic import BaseSettings as BSettings


class BaseSettings(BSettings):
    LANGUAGE_CODE: str = 'en'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return BaseSettings()


BASE_SETTINGS = get_settings()
