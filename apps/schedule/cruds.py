from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from apps.schedule.models import Schedule
from apps.schedule.schemas import ScheduleCreate, ScheduleUpdate

async def get_schedule(db: AsyncSession, schedule_id: int):
    result = await db.execute(select(Schedule).filter(Schedule.id == schedule_id))
    return result.scalars().first()

async def get_schedules(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Schedule).offset(skip).limit(limit))
    return result.scalars().all()

async def create_schedule(db: AsyncSession, schedule: ScheduleCreate):
    db_schedule = Schedule(**schedule.model_dump())
    db.add(db_schedule)
    await db.commit()
    await db.refresh(db_schedule)
    return db_schedule

async def update_schedule(db: AsyncSession, schedule_id: int, schedule: ScheduleUpdate):
    db_schedule = await get_schedule(db, schedule_id)
    if not db_schedule:
        return None
    update_data = schedule.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_schedule, key, value)
    await db.commit()
    await db.refresh(db_schedule)
    return db_schedule

async def delete_schedule(db: AsyncSession, schedule_id: int):
    db_schedule = await get_schedule(db, schedule_id)
    if not db_schedule:
        return False
    await db.delete(db_schedule)
    await db.commit()
    return True
