"""Add events table

Revision ID: dbb3afe4c92b
Revises: 542867686f77
Create Date: 2024-03-17 16:28:38.276193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbb3afe4c92b'
down_revision: Union[str, None] = '542867686f77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('meeting_time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'meeting_time')
    # ### end Alembic commands ###
