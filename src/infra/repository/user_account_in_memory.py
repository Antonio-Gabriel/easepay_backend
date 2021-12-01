from datetime import datetime
from typing import Type, Union
from uuid import uuid4

from ...domain.repositories import IAccountRepository
from ...domain.entities import UserAccount


class UserAccountInMemoryRepository(IAccountRepository):
    def __init__(self):
        self.__storage = [
            {
                "id": str(uuid4()),
                "name": "Antonio Gabriel",
                "email": "antoniogabriel@gmail.com",
                "password": b"7bd609ad1b5a0c4a52c012263801539c1235cf4f",
                "permition_code": 99834,
                "phone": [989834555, 982345222],
                "wallet": 0,
                "state": True,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        ]

    def create_account(self, user_account: Type[UserAccount]) -> Union[list, dict]:
        """Create a new account"""

        try:
            hash_pass = user_account.account.password_encrypt()
            self.__storage.append(
                {
                    "id": str(uuid4()),
                    "name": user_account.user.full_name,
                    "email": user_account.user.email,
                    "password": hash_pass,
                    "permition_code": user_account.account.permition_code,
                    "phone": user_account.user.phone_number.phone,
                    "wallet": user_account.wallet.amount,
                    "state": user_account.state,
                    "created_at": user_account.created_at,
                    "updated_at": user_account.updated_at,
                }
            )

            return self.__storage
        except Exception as ex:
            return {"error": ex.args}

    def update_account(self, user_account: Type[UserAccount]) -> UserAccount:
        """Update account"""

        hash_pass = user_account.account.password_encrypt()        
        object_assigned = {
            **self.__storage[0],
            "name": user_account.user.full_name,
            "email": user_account.user.email,
            "password": hash_pass,
            "permition_code": user_account.account.permition_code,
            "phone": user_account.user.phone_number.phone,
            "updated_at": user_account.updated_at,
        }

        self.__storage[0] = object_assigned

        return self.__storage
