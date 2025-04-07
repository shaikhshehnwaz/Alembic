"""Initail

Revision ID: 95bcbe83ef4a
Revises: 
Create Date: 2025-02-18 10:30:38.061985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95bcbe83ef4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('user', sa.Column('phone_no', sa.String(length=100), nullable=True))


def downgrade():
    op.drop_column('user', 'phone_no')
