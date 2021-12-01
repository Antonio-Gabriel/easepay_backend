from typing import Type

from ...repositories import IAccountRepository


class ForgotUserAccount:
    def __init__(self, user_account_interface: Type[IAccountRepository]):
        self.__iuser_account = user_account_interface

    def execute(self, email_address: str) -> list:
        """forgot user account"""

        return self.__iuser_account.forgot_account(email_address)
