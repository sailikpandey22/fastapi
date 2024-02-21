"""Add content column to post table

Revision ID: a5570d67b6d6
Revises: 56847151b258
Create Date: 2024-02-22 01:43:16.043423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5570d67b6d6'
down_revision: Union[str, None] = '56847151b258'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
