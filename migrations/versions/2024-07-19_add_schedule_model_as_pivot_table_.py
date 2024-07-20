"""Add Schedule model as pivot table between movie and room

Revision ID: 084e00db41ef
Revises: 9e0f67121d8b
Create Date: 2024-07-19 23:46:07.560061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '084e00db41ef'
down_revision: Union[str, None] = '9e0f67121d8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schedules_id'), 'schedules', ['id'], unique=False)
    op.add_column('bookings', sa.Column('schedule_id', sa.Integer(), nullable=False))
    op.drop_constraint('bookings_movie_id_fkey', 'bookings', type_='foreignkey')
    op.drop_constraint('bookings_room_id_fkey', 'bookings', type_='foreignkey')
    op.create_foreign_key(None, 'bookings', 'schedules', ['schedule_id'], ['id'], ondelete='CASCADE')
    op.drop_column('bookings', 'movie_id')
    op.drop_column('bookings', 'room_id')
    op.drop_constraint('movies_room_id_fkey', 'movies', type_='foreignkey')
    op.drop_column('movies', 'room_id')
    op.drop_column('movies', 'start_time')
    op.drop_column('movies', 'end_time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('end_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('movies', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('movies', sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('movies_room_id_fkey', 'movies', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.add_column('bookings', sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('bookings', sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'bookings', type_='foreignkey')
    op.create_foreign_key('bookings_room_id_fkey', 'bookings', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('bookings_movie_id_fkey', 'bookings', 'movies', ['movie_id'], ['id'], ondelete='CASCADE')
    op.drop_column('bookings', 'schedule_id')
    op.drop_index(op.f('ix_schedules_id'), table_name='schedules')
    op.drop_table('schedules')
    # ### end Alembic commands ###