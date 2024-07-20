from sqlalchemy.ext.asyncio import AsyncSession

from apps.movie.models import Movie
from apps.movie.schemas import MovieCreate, MovieUpdate


async def get_movie(db: AsyncSession, movie_id: int):
    return await db.get(Movie, movie_id)


async def create_movie(db: AsyncSession, movie: MovieCreate):
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    await db.commit()
    await db.refresh(db_movie)
    return db_movie


async def update_movie(db: AsyncSession, movie_id: int, movie: MovieUpdate):
    db_movie = await get_movie(db, movie_id)
    if not db_movie:
        return None
    for key, value in movie.model_dump(exclude_unset=True).items():
        setattr(db_movie, key, value)
    await db.commit()
    await db.refresh(db_movie)
    return db_movie


async def delete_movie(db: AsyncSession, movie_id: int):
    db_movie = await get_movie(db, movie_id)
    if not db_movie:
        return False
    await db.delete(db_movie)
    await db.commit()
    return True
