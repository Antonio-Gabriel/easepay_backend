from datetime import datetime
from dataclasses import dataclass, fields

from ..entities import Account, Owner, Studant


@dataclass(frozen=True)
class IUserAccountRequestDto:
    account: Account
    owber: Owner
    student: Studant
    state: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        """Raise exception"""

        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type} but got {repr(value)}"
                )
