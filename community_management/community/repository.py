import os
from typing import Dict, Any

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import Session

from community_management.community.community import CommunityTable


class CommunityRepository:
    def __init__(self) -> None:
        # TODO: тут надо переписать на получение AsyncSession
        hostname = os.environ.get("DATABASE_HOSTNAME", "localhost")
        self._engine = create_engine(url=f"postgresql+psycopg2://admin:admin@{hostname}:5432/admin")
        CommunityTable.metadata.create_all(self._engine)

    def exists(self, id_: int) -> bool:
        with Session(self._engine) as session:
            return session.query(exists().where(CommunityTable.id == id_)).scalar()

    def get(self, id_: int) -> Dict[str, Any]:
        with Session(self._engine) as session:
            return session.query(CommunityTable).filter(CommunityTable.id == id_).first().__dict__

    def add(self, community: Dict[str, Any]) -> Dict[str, Any]:
        with Session(self._engine) as session:
            session.add(CommunityTable(**community))
            session.commit()
        return self.get(id_=community["id"])

    def delete(self, id_: int) -> None:
        with Session(self._engine) as session:
            community = session.query(CommunityTable).filter(CommunityTable.id == id_).first()
            session.delete(community)
            session.commit()
