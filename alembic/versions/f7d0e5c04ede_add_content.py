"""add content

Revision ID: f7d0e5c04ede
Revises: 3e1cb648b95c
Create Date: 2026-09-21 12:49:20.246611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7d0e5c04ede'
down_revision: Union[str, Sequence[str], None] = '3e1cb648b95c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'content')
