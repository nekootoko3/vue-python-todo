"""Create todos

Revision ID: ef7ceebc0d3a
Revises: d58572bc9fc8
Create Date: 2020-08-29 09:51:08.170715

"""
from alembic import op
from sqlalchemy import text
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef7ceebc0d3a'
down_revision = 'd58572bc9fc8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime()),
        sa.Column("updated_at", sa.DateTime()),
    )


def downgrade():
    op.drop_table("todos")
