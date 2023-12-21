"""added country on user

Revision ID: dd5d253fe9da
Revises: a0d1d071e6af
Create Date: 2023-12-20 21:21:53.470869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd5d253fe9da'
down_revision: Union[str, None] = 'a0d1d071e6af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'country')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('country', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###