"""Database creation

Revision ID: d3eabc409443
Revises:
Create Date: 2024-04-20 22:04:35.204701

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d3eabc409443"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "last_operation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("operation", sa.String(length=255), nullable=True),
        sa.Column("timestamp", sa.TIMESTAMP(), nullable=True),
        sa.Column("status_ok", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=15), nullable=False),
        sa.Column("task_enable", sa.Integer(), nullable=True),
        sa.Column("check_interval", sa.Integer(), nullable=True),
        sa.Column("last_operation_id", sa.Integer(), nullable=True),
        sa.Column("notes", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["last_operation_id"],
            ["last_operation.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "from_dirs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=True),
        sa.Column("path_from_dir", sa.String(length=255), nullable=True),
        sa.Column("file_extensions", sa.String(length=255), nullable=True),
        sa.Column("del_after_copy", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "to_dirs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=True),
        sa.Column("path_to_dir", sa.String(length=255), nullable=True),
        sa.Column("create_dir_day", sa.Integer(), nullable=True),
        sa.Column("create_dir_hour", sa.Integer(), nullable=True),
        sa.Column("create_dir_extension", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "file_extensions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("from_dir_id", sa.Integer(), nullable=True),
        sa.Column("extension", sa.String(length=255), nullable=True),
        sa.Column("min_size_file", sa.Integer(), nullable=True),
        sa.Column("max_size_file", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["from_dir_id"],
            ["from_dirs.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file_extensions")
    op.drop_table("to_dirs")
    op.drop_table("from_dirs")
    op.drop_table("tasks")
    op.drop_table("last_operation")
    # ### end Alembic commands ###
