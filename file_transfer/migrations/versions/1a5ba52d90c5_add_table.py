"""add table

Revision ID: 1a5ba52d90c5
Revises: a90eeb4405ae
Create Date: 2024-04-24 20:09:09.141770

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1a5ba52d90c5"
down_revision: Union[str, None] = "a90eeb4405ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "from_dir",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("path_from_dir", sa.String(), nullable=False),
        sa.Column("file_extensions_to_copy", sa.JSON(), nullable=False),
        sa.Column("del_after_copy", sa.Boolean(), nullable=True),
        sa.Column("not_copy_extensions", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "last_operation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("operation", sa.String(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("status_ok", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "to_dir",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("path_to_dir", sa.String(), nullable=False),
        sa.Column("create_dir_day", sa.Boolean(), nullable=True),
        sa.Column("create_dir_hour", sa.Boolean(), nullable=True),
        sa.Column("create_dir_extension", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "file_extension",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("from_dir_id", sa.Integer(), nullable=False),
        sa.Column("extension", sa.String(), nullable=False),
        sa.Column("min_size_file", sa.Integer(), nullable=False),
        sa.Column("max_size_file", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["from_dir_id"],
            ["from_dir.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "file_extension_not_copy",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("from_dir_id", sa.Integer(), nullable=False),
        sa.Column("extension", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["from_dir_id"],
            ["from_dir.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file_extension_not_copy")
    op.drop_table("file_extension")
    op.drop_table("to_dir")
    op.drop_table("last_operation")
    op.drop_table("from_dir")
    # ### end Alembic commands ###
