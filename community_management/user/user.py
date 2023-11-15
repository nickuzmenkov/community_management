from pydantic import BaseModel, Field
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "User"

    username: Mapped[str] = mapped_column(String(255), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255))
    age: Mapped[int]


class UserModel(BaseModel):
    username: str = Field(min_length=3, max_length=255, pattern="^[a-z0-9_]+$", examples=["john_doe007"])
    full_name: str = Field(min_length=3, max_length=255, examples=["John Doe"])
    age: int = Field(ge=1, examples=[38])
