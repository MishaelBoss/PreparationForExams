from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
import sqlalchemy as sa


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    usename: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))
    password: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))

    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.text("CURRENT_TIMESTAMP")}
    )