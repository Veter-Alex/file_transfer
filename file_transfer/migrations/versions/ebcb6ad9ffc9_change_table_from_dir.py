"""change table From_dir

Revision ID: ebcb6ad9ffc9
Revises: 56fccfd50653
Create Date: 2024-04-24 21:13:29.095595

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "ebcb6ad9ffc9"
down_revision: Union[str, None] = "56fccfd50653"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("from_dir", "file_extensions_to_copy")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "from_dir",
        sa.Column(
            "file_extensions_to_copy",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
    )
    # ### end Alembic commands ###
