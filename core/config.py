from typing import Any

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENABLE_DEBUG: bool = False
    ENVIRONMENT: str = 'dev'

    ECHO_SQL: bool = False
    DATABASE_SCHEME: str = 'postgresql+asyncpg'
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    ASYNC_DATABASE_URI: PostgresDsn | str = ''

    @field_validator('ASYNC_DATABASE_URI', mode='after')
    def assemble_db_connection(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str) and v == '':
            return PostgresDsn.build(
                scheme=info.data['DATABASE_SCHEME'],
                username=info.data['DATABASE_USER'],
                password=info.data['DATABASE_PASS'],
                host=info.data['DATABASE_HOST'],
                port=info.data['DATABASE_PORT'],
                path=info.data['DATABASE_NAME'],
            )
        return v

    class ConfigDict:
        env_file = '.env'


settings = Settings()
