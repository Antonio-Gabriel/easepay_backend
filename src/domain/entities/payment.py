from .user import User
from typing import Type
from decimal import Decimal
from datetime import datetime


class Payment:
    def __init__(
        self,
        value: Decimal,
        user: Type[User],
        created_at: datetime,
        updated_at: datetime,
        id: int = None,
    ):
        self.id = id
        self.value = value
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at
