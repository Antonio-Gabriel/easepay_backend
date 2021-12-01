from abc import ABC, abstractmethod
from typing import List, Type, Union

from ..entities import UserAccount


class IAccountRepository(ABC):
    @abstractmethod
    def create_account(
        user_account: Type[UserAccount],
    ) -> Union[List[UserAccount], dict]:
        """Create a new account"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def update_account(user_account: Type[UserAccount]) -> UserAccount:
        """Update account"""

        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def forgot_account(email_address: str) -> List[UserAccount]:
        """Forget account"""

        raise NotImplementedError("This method is not implemented")
