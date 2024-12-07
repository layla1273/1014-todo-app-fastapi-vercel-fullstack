"""create todos table

Revision ID: e21fb577b56b
Revises: ad1c380734f8
Create Date: 2024-12-07 16:29:24.921857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e21fb577b56b'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
