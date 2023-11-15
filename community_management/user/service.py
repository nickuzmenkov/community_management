from community_management.user.user import UserModel
from community_management.user.repository import UserRepository


class UserNotFoundError(Exception):
    pass


class UserExistsError(Exception):
    pass


class UserService:
    def __init__(self) -> None:
        self._repository = UserRepository()

    def exists(self, username: str) -> bool:
        return self._repository.exists(username=username)

    def add(self, user: UserModel) -> UserModel:
        if self.exists(username=user.username):
            raise UserExistsError(f"User with username '{user.username}' already exists.")
        self._repository.add(user=user.model_dump())
        user_dict = self._repository.get(username=user.username)
        return UserModel.model_validate(user_dict)

    def get(self, username: str) -> UserModel:
        if not self.exists(username=username):
            raise UserNotFoundError(f"User with username '{username}' is not found.")
        user_dict = self._repository.get(username=username)
        return UserModel.model_validate(user_dict)

    def delete(self, username: str) -> None:
        if not self.exists(username=username):
            raise UserNotFoundError(f"User with username '{username}' is not found.")
        self._repository.delete(username=username)
