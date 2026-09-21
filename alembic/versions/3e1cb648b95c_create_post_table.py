"""create post table

Revision ID: 3e1cb648b95c
Revises: 
Create Date: 2026-09-21 12:28:44.627857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e1cb648b95c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False),
    )


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'title')
