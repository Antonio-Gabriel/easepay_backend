from typing import Type
from ...domain.repositories import IAccountRepository

from ...domain.entities import UserAccount


class UserAccountInMemoryRepository(IAccountRepository):
    def __init__(self):
        pass

    def create_account(self, user_account: Type[UserAccount]) -> UserAccount:
        """Create a new account"""

        hash_pass = user_account.account.password_encrypt()
        print(user_account.user.full_name, hash_pass)

    def update_account(user_account: Type[UserAccount]) -> UserAccount:
        """Update account"""

        pass
