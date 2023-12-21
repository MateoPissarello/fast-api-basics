"""updated model

Revision ID: 0ea52d898da4
Revises: 069d2b0b0cb8
Create Date: 2023-12-20 21:20:18.790153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ea52d898da4'
down_revision: Union[str, None] = '069d2b0b0cb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
