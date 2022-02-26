from abc import ABC, abstractmethod
from typing import List, Type, Union

from ..entities import User


class IUserRepository(ABC):
    @abstractmethod
    def create_account(
        user: Type[User],
    ) -> Union[List[User], dict]:
        """Create a new account"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def update_account(user: Type[User]) -> User:
        """Update account"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def get() -> User:
        """Get all users"""

        raise NotImplementedError("This method is not implemented")

    def get_by_id(user_id: int) -> User:
        """Get especitic user by id"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def forgot_account(email_address: str) -> List[User]:
        """Forget account"""

        raise NotImplementedError("This method is not implemented")
