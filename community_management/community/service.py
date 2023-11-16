from community_management.community.schemas import CommunityInputModel, CommunityModel
from community_management.community.repository import CommunityRepository


class CommunityNotFoundError(Exception):
    pass


class CommunityService:
    def __init__(self) -> None:
        self._repository = CommunityRepository()

    def exists(self, id_: int) -> bool:
        return self._repository.exists(id_)

    def add(self, community: CommunityInputModel) -> CommunityModel:
        community_dict = self._repository.add(community=community.model_dump())
        return CommunityModel.model_validate(community_dict)

    def get(self, id_: int) -> CommunityModel:
        if not self.exists(id_):
            raise CommunityNotFoundError(f"Community with ID {id_} is not found.")
        community_dict = self._repository.get(id_)
        return CommunityModel.model_validate(community_dict)

    def delete(self, id_: int) -> None:
        if not self.exists(id_):
            raise CommunityNotFoundError(f"Community with ID {id_} is not found.")
        self._repository.delete(id_)
