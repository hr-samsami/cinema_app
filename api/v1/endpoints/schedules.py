# cinema_app/api/api_v1/endpoints/schedule.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from crud.schedules import get_schedule, get_schedules, create_schedule, update_schedule, delete_schedule
from schemas.schedule import Schedule, ScheduleCreate, ScheduleUpdate
from api.dependencies.db import get_db

router = APIRouter()

@router.get("/", response_model=List[Schedule])
async def read_schedules(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_schedules(db=db, skip=skip, limit=limit)

@router.post("/", response_model=Schedule)
async def create_schedule(schedule_in: ScheduleCreate, db: AsyncSession = Depends(get_db)):
    return await create_schedule(db=db, schedule=schedule_in)

@router.put("/{schedule_id}", response_model=Schedule)
async def update_schedule(schedule_id: int, schedule_in: ScheduleUpdate, db: AsyncSession = Depends(get_db)):
    db_schedule = await get_schedule(db=db, schedule_id=schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return await update_schedule(db=db, schedule_id=schedule_id, schedule=schedule_in)

@router.delete("/{schedule_id}", response_model=Schedule)
async def delete_schedule(schedule_id: int, db: AsyncSession = Depends(get_db)):
    db_schedule = await get_schedule(db=db, schedule_id=schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    await delete_schedule(db=db, schedule_id=schedule_id)
    return db_schedule