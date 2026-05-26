"""drop poll edit_responses_until

Revision ID: 7a2c4f9e8b13
Revises: 3f8a1b2c5d7e
Create Date: 2026-05-26 12:00:00

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "7a2c4f9e8b13"
down_revision: str | None = "3f8a1b2c5d7e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_column("polls", "edit_responses_until")


def downgrade() -> None:
    op.add_column(
        "polls",
        sa.Column("edit_responses_until", sa.DateTime(timezone=True), nullable=True),
    )
