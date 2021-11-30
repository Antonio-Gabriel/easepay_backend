from typing import Type

from ...dto import IUserAccountRequestDto
from ...repositories import IAccountRepository

from ....adapters import UserAccountAdapter


class CreateAccount:
    def __init__(self, user_account_interface: Type[IAccountRepository]):
        self.__iuser_account = user_account_interface

    def execute(self, user_account: Type[IUserAccountRequestDto]):
        """Create account

        Args:
            user_account (Type[IUserAccountRequestDto]): return created user
        """

        user_account_adp = UserAccountAdapter()
        adapter_instance = user_account_adp.create(
            user_account.account.permition_code,
            user_account.account.password,
            user_account.user.full_name,
            user_account.user.email,
            user_account.user.phone_number.phone,
        )

        if not adapter_instance.is_null_or_empty_attr():
            raise Exception("Verify empty value")

        if not user_account.account.is_valid_permition_code():
            raise Exception("Permition code is invalid")

        if not user_account.user.is_valid_email_address():
            raise Exception("Invalid email, pleace check the email...")

        self.__iuser_account.create_account(adapter_instance)
