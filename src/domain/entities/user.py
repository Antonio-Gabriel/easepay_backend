import re


class User:
    def __init__(self, full_name: str, email: str, id: int = None):
        self.id = id
        self.full_name = full_name
        self.email = email

    def is_valid_email_address(self) -> bool:
        """ Verify if the email address is valid"""

        expretion = r"^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$"
        return True if re.search(expretion, self.email) is not None else False
