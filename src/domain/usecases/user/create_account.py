from typing import Type

from ...dto import IUserAccountRequestDto
from ...repositories import IAccountRepository

from ....adapters import UserAccountAdapter


class CreateAccount:
    def __init__(self, user_account_interface: Type[IAccountRepository]):
        self.__iuser_account = user_account_interface

    def execute(self, user_account: Type[IUserAccountRequestDto]) -> list:
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
            user_account.wallet.amount,
        )

        adapter_instance.created_at = user_account.created_at
        adapter_instance.updated_at = user_account.updated_at

        if not adapter_instance.is_null_or_empty_attr():
            raise Exception("Verify empty value")

        if not user_account.account.is_valid_permition_code():
            raise Exception("Permition code is invalid")

        if not user_account.user.is_valid_email_address():
            raise Exception("Invalid email, pleace check the email...")

        if not user_account.user.phone_number.is_valid_phone_number_of_list():
            raise Exception("Phone number is invalid")

        return self.__iuser_account.create_account(adapter_instance)
