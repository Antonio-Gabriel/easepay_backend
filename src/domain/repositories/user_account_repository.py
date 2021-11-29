from abc import ABC, abstractmethod
from typing import Type

from ..entities import UserAccount


class IAccountRepository(ABC):
    @abstractmethod
    def create_account(user_account: Type[UserAccount]) -> UserAccount:
        """Create a new account"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def update_account(user_account: Type[UserAccount]) -> UserAccount:
        """Update account"""

        raise NotImplementedError("This method is not implemented")
