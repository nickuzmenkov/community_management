from fastapi import APIRouter, Depends, HTTPException

from community_management.community.service import CommunityService, CommunityNotFoundError
from community_management.community.schemas import CommunityModel, CommunityInputModel

community_router = APIRouter(prefix="/communities")


@community_router.post("/")
# TODO: async
def create_community(community: CommunityInputModel, service: CommunityService = Depends(CommunityService)) -> CommunityModel:
    return service.add(community)


@community_router.get("/{id}")
def get_community(id: int, service: CommunityService = Depends(CommunityService)) -> CommunityModel:
    try:
        return service.get(id)
    except CommunityNotFoundError as exception:
        raise HTTPException(status_code=404, detail=str(exception))


@community_router.delete("/{id}")
def delete_community(id: int, service: CommunityService = Depends(CommunityService)) -> None:
    try:
        service.delete(id)
    except CommunityNotFoundError as exception:
        raise HTTPException(status_code=404, detail=str(exception))
