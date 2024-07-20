from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.db import get_db
from api.exceptions import MovieNotFoundException
from crud.movies import create_movie, delete_movie, get_movie, update_movie
from schemas.movie import Movie, MovieCreate, MovieUpdate

router = APIRouter()


@router.get('/{movie_id}', response_model=Movie)
async def read_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    db_movie = await get_movie(db, movie_id)
    if not db_movie:
        raise MovieNotFoundException()
    return db_movie


@router.post('/', response_model=Movie)
async def create_new_movie(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    return await create_movie(db, movie)


@router.put('/{movie_id}', response_model=Movie)
async def update_existing_movie(movie_id: int, movie: MovieUpdate, db: AsyncSession = Depends(get_db)):
    db_movie = await update_movie(db, movie_id, movie)
    if not db_movie:
        raise MovieNotFoundException()
    return db_movie


@router.delete('/{movie_id}', response_model=bool)
async def delete_existing_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_movie(db, movie_id)
    if not success:
        raise MovieNotFoundException()
    return True
