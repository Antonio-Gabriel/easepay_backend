from decimal import Decimal
from typing import List
from ..domain.entities import User, Account, Owner, Studant


class UserAccountAdapter:
    @staticmethod
    def create(username: str, password: str, name: str, phone: str, email: str):
        """Useraccount adapter"""

        return User(
            account=Account(username, password),
            owner=Owner(name, phone, email),
            studant=Studant()
        )                        
       
