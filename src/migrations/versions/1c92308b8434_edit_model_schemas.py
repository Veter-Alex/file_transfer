"""edit model schemas

Revision ID: 1c92308b8434
Revises: 737285099091
Create Date: 2024-05-10 19:47:20.282056

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "1c92308b8434"
down_revision: Union[str, None] = "737285099091"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "last_operations",
        "operation",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    op.alter_column(
        "last_operations",
        "timestamp",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
    )
    op.add_column("tasks", sa.Column("is_run", sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, "tasks", ["title"])
    op.drop_column("tasks", "task_enable")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tasks",
        sa.Column(
            "task_enable", sa.BOOLEAN(), autoincrement=False, nullable=True
        ),
    )
    op.drop_constraint(None, "tasks", type_="unique")
    op.drop_column("tasks", "is_run")
    op.alter_column(
        "last_operations",
        "timestamp",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    op.alter_column(
        "last_operations",
        "operation",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    # ### end Alembic commands ###