"""add few cols to post tabel

Revision ID: 64e888bfefc9
Revises: ac65a577c22c
Create Date: 2026-09-21 13:22:32.969486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64e888bfefc9'
down_revision: Union[str, Sequence[str], None] = 'ac65a577c22c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False,
                                     server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                     nullable=False, server_default=sa.text('now()')))


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
