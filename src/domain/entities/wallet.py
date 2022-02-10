import datetime
from .user import User
from typing import Type
from _decimal import Decimal


class Wallet:
    def __init__(
        self,
        user: Type[User],
        created_at: datetime,
        updated_at: datetime,
        balance: Decimal = 0.00,
        id: int = None,
    ):
        self.id = id
        self.balance = balance
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at

    def deposit(self, amount_to_deposit: float):
        """Add ammount to the wallet"""

        self.balance += amount_to_deposit
        return self.amount

    def with_draw(self, amount_to_withdraw: float):
        """remove amount to the wallet"""

        self.balance -= amount_to_withdraw
        return self.balance
