import re
from typing import Type

from .phone_number import PhoneNumber


class User:
    def __init__(
        self,
        full_name: str,
        email: str,
        phone_number: Type[PhoneNumber],
        id: int = None,
    ):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number

    def is_valid_email_address(self) -> bool:
        """Verify if the email address is valid"""

        expretion = r"^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$"
        return True if re.search(expretion, self.email) is not None else False
