from datetime import datetime

from sqlalchemy import String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from community_management.community.constants import TopicKind

from community_management.user.user import UserTable


class Base(DeclarativeBase):
    pass


class CommunityTable(Base):
    __tablename__ = "Community"  # с маленькой буквы названия таблиц в БД (если словосочетание - community_management)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    topic: Mapped[str] = mapped_column(String(255))
    owner_username: Mapped[str] = mapped_column(ForeignKey(UserTable.username))
    adult_only: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
