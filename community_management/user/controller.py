from fastapi import APIRouter, Depends, HTTPException

from community_management.user.service import UserService, UserExistsError, UserNotFoundError
from community_management.user.user import UserModel

user_router = APIRouter(prefix="/users")


@user_router.post("/")
def create_user(user: UserModel, service: UserService = Depends(UserService)) -> UserModel:
    try:
        return service.add(user=user)
    except UserExistsError as exception:
        raise HTTPException(status_code=403, detail=str(exception))


@user_router.get("/{username}")
def get_user(username: str, service: UserService = Depends(UserService)) -> UserModel:
    try:
        return service.get(username=username)
    except UserNotFoundError as exception:
        raise HTTPException(status_code=404, detail=str(exception))


@user_router.delete("/")
def delete_user(username: str, service: UserService = Depends(UserService)) -> None:
    try:
        service.delete(username=username)
    except UserNotFoundError as exception:
        raise HTTPException(status_code=404, detail=str(exception))
