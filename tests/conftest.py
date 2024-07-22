import os
import sys

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.dependencies import get_db
from core.model_base import Base
from main import app as fastapi_app

DATABASE_URL = 'postgresql+asyncpg://postgres:pass@localhost:5432/cinema_test'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


@pytest.fixture(scope='module')
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='module')
async def client(db_session):
    fastapi_app.dependency_overrides[get_db] = lambda: db_session
    async with AsyncClient(app=fastapi_app, base_url='http://localhost:8000') as client:
        yield client
