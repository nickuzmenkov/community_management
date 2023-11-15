import os
from typing import Dict, Any

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import Session

from community_management.user.user import UserTable


class UserRepository:
    def __init__(self) -> None:
        hostname = os.environ.get("DATABASE_HOSTNAME", "localhost")
        self._engine = create_engine(url=f"postgresql+psycopg2://admin:admin@{hostname}:5432/admin")
        UserTable.metadata.create_all(self._engine)

    def exists(self, username: str) -> bool:
        with Session(self._engine) as session:
            return session.query(exists().where(UserTable.username == username)).scalar()

    def get(self, username: str) -> Dict[str, Any]:
        with Session(self._engine) as session:
            return session.query(UserTable).filter(UserTable.username == username).first().__dict__

    def add(self, user: Dict[str, Any]) -> Dict[str, Any]:
        with Session(self._engine) as session:
            session.add(UserTable(**user))
            session.commit()
        return self.get(username=user["username"])

    def delete(self, username: str) -> None:
        with Session(self._engine) as session:
            user = session.query(UserTable).filter(UserTable.username == username).first()
            session.delete(user)
            session.commit()
