from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field
from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from community_management.user.user import UserTable


class Base(DeclarativeBase):
    pass


class TopicKind(str, Enum):
    FUN = "fun"
    MOVIES = "movies"
    SCIENCE = "science"
    SPORTS = "sports"


class CommunityTable(Base):
    __tablename__ = "Community"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    topic: Mapped[str] = mapped_column(String(255))
    owner_username: Mapped[str] = mapped_column(ForeignKey(UserTable.username))
    adult_only: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)


class CommunityInputModel(BaseModel):
    name: str = Field(min_length=3, max_length=255, examples=[])
    topic: TopicKind = Field(examples=[TopicKind.MOVIES])
    owner_username: str = Field(min_length=3, max_length=255, examples=["John Doe"])
    adult_only: bool = False


class CommunityModel(CommunityInputModel):
    id: int = Field(ge=1)
    created_at: datetime
