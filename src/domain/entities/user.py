import datetime
from typing import Type

from .owner import Owner
from .account import Account
from .student import Studant


class User:
    def __init__(
        self,
        account: Type[Account],
        owner: Type[Owner],
        studant: Type[Studant],
        created_at: datetime,
        updated_at: datetime,
        state: bool = True,
        id: int = None,
    ):
        self.id = id
        self.account = account
        self.owner = owner
        self.studant = studant
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
