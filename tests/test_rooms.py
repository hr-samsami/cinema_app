import pytest
from httpx import AsyncClient

from core.init_db import SessionLocal, init_db
from main import app


@pytest.fixture(scope='module')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        await init_db()
        yield ac


@pytest.fixture(scope='module')
async def db_session():
    async with SessionLocal() as session:
        yield session


@pytest.mark.asyncio
async def test_create_room(client: AsyncClient):
    response = await client.post('/rooms/', json={'name': 'Red Room', 'rows': 10, 'seats_per_row': 8})
    assert response.status_code == 200
    assert response.json()['name'] == 'Red Room'


@pytest.mark.asyncio
async def test_read_room(client: AsyncClient):
    response = await client.get('/rooms/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Red Room'


@pytest.mark.asyncio
async def test_update_room(client: AsyncClient):
    response = await client.put('/rooms/1', json={'name': 'Blue Room', 'rows': 12, 'seats_per_row': 10})
    assert response.status_code == 200
    assert response.json()['name'] == 'Blue Room'


@pytest.mark.asyncio
async def test_delete_room(client: AsyncClient):
    response = await client.delete('/rooms/1')
    assert response.status_code == 200
    assert response.json() is True
