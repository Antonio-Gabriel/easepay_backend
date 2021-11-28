import datetime
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
        updated_at: datetime = None,
        created_at: datetime = None,
    ):
        self.account = account
        self.user = user
        self.wallet = wallet
        self.state = state
        self.updated_at = created_at
        self.updated_at = updated_at

    def is_null_or_empty_attr(self):
        """verify null or empty attribute"""

        if not (
            self.account.permition_code > 0
            and self.account.password != ""
            and self.user.full_name != ""
            and self.user.email != ""
        ):
            return False

        return True
