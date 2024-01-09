from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class BaseUUIDModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)


class BaseModel(BaseUUIDModel):
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )
