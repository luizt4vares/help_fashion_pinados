from pydantic import BaseSettings

class Settings(BaseSettings):
    PRESTO_HOST: str = ""
    PRESTO_PORT: str = ""
    PRESTO_USERNAME: str = ""
    PRESTO_PASSWORD: str = ""

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings()