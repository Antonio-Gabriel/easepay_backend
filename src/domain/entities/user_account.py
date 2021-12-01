from datetime import datetime
from typing import Type

from .wallet import Wallet
from .user import User
from .account import Account


class UserAccount:
    def __init__(
        self,
        account: Type[Account],
        user: Type[User],
        wallet: Type[Wallet],
        state: bool = True,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        self.account = account
        self.user = user
        self.wallet = wallet
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at

    def is_null_or_empty_attr(self):
        """verify null or empty attribute"""

        if not (
            self.account.password != ""
            and self.user.full_name != ""
            and self.user.email != ""
        ):
            return False

        return True
