"""create_book_model

Revision ID: b9f3ae593c8e
Revises: dc99fbf463d0
Create Date: 2024-01-09 16:05:48.510184

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = "b9f3ae593c8e"
down_revision = "dc99fbf463d0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "book",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("full_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("short_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("book_type", sa.Enum("NT", "OT", name="bookenum"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("full_name"),
        sa.UniqueConstraint("short_name"),
    )
    op.create_index(op.f("ix_book_id"), "book", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_book_id"), table_name="book")
    op.drop_table("book")
    # ### end Alembic commands ###
