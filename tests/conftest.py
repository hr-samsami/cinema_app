from typing import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import StaticPool, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from apps.room.models import Room
from core.dependencies import get_db
from core.model_base import Base

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATABASE_URL = 'postgresql+asyncpg://postgres:pass@localhost:5432/cinema_test'
from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from main import app

engine = create_async_engine(
    url='postgresql+asyncpg://postgres:nemesis@localhost:5432/cinema_test',
    echo=False,
)


# drop all database every time when test complete
@pytest_asyncio.fixture(scope='function')
async def async_engine():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope='function')
async def async_db(async_engine):
    async_session_factory = sessionmaker(
        async_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    async with async_session_factory() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()


app.dependency_overrides[get_db] = async_db


@pytest_asyncio.fixture(scope='function')
async def async_room_orm(async_db: AsyncSession) -> Room:
    room = Room(
        name='red',
        rows=12,
        seats_per_row=20,
    )
    async_db.add(room)
    await async_db.commit()
    await async_db.refresh(room)
    return room


@pytest_asyncio.fixture(scope='function')
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://localhost:8000') as client:
        yield client
