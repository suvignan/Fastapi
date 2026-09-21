"""add phone number

Revision ID: 3c9c7d8b2e3f
Revises: cfea14bf1cbb
Create Date: 2026-09-21 13:31:30.718018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c9c7d8b2e3f'
down_revision: Union[str, Sequence[str], None] = 'cfea14bf1cbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
