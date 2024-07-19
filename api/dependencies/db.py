from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.init_db import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
