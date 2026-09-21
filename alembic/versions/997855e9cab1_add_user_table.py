"""add user table

Revision ID: 997855e9cab1
Revises: f7d0e5c04ede
Create Date: 2026-09-21 12:56:05.864566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '997855e9cab1'
down_revision: Union[str, Sequence[str], None] = 'f7d0e5c04ede'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
              sa.PrimaryKeyConstraint('id'),
              sa.UniqueConstraint('email')
    )


def downgrade():
    """Downgrade schema."""
    op.drop_table('users')