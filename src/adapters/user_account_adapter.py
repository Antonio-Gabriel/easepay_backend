from typing import List
from ..domain.entities import UserAccount, User, Account, Wallet, PhoneNumber


class UserAccountAdapter:
    @staticmethod
    def create(
        permition_code: int, password: str, full_name: str, email: str, phone: List[int]
    ):
        """Useraccount adapter"""

        return UserAccount(
            account=Account(permition_code, password),
            user=User(full_name, email, PhoneNumber(phone)),
            wallet=Wallet(),
        )