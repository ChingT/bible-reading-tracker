"""create_schedule_model

Revision ID: 4868fade9a9f
Revises: abab2b78b44f
Create Date: 2024-01-10 12:09:26.506129

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = "4868fade9a9f"
down_revision = "abab2b78b44f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "schedule",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("plan_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(
            ["plan_id"],
            ["plan.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("date"),
    )
    op.create_index(op.f("ix_schedule_id"), "schedule", ["id"], unique=False)
    op.create_table(
        "schedule_passage_link",
        sa.Column("schedule_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("passage_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["schedule_id"],
            ["schedule.id"],
        ),
        sa.ForeignKeyConstraint(
            ["passage_id"],
            ["passage.id"],
        ),
        sa.PrimaryKeyConstraint("schedule_id", "passage_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("schedule_passage_link")
    op.drop_index(op.f("ix_schedule_id"), table_name="schedule")
    op.drop_table("schedule")
    # ### end Alembic commands ###
