import pytest
from fastapi import FastAPI, status
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.room.models import Room

pytestmark = pytest.mark.asyncio


async def test_main(client: AsyncClient) -> None:
    response = await client.get('/docs')
    assert response.status_code == status.HTTP_200_OK


async def test_get_room(client: AsyncClient, async_db: AsyncSession, async_room_orm: Room):
    response = await client.get(f'/admin/rooms/{async_room_orm.id}')

    assert response.status_code == status.HTTP_200_OK

    db_room = await async_db.execute(select(Room).filter(Room.id == async_room_orm.id))
    fetched_room = db_room.scalar_one()

    assert fetched_room.id == async_room_orm.id


# async def test_update_example(async_client: AsyncClient, async_db: AsyncSession,
#                               async_example_orm: Example) -> None:
#     payload = {'name': 'updated_name', 'age': 20}

#     response = await async_client.put(f'/api/async-examples/{async_example_orm.id}',
#                                       json=payload)
#     assert response.status_code == status.HTTP_200_OK
#     await async_db.refresh(async_example_orm)
#     assert (await
#             async_db.execute(select(Example).filter_by(id=async_example_orm.id)
#                             )).scalar_one().name == response.json()['data']['name']
