from typing import Type

from ...repositories import IAccountRepository
from ...dto import IUserAccountRequestDto

from ....adapters import UserAccountAdapter

from ...validator import Email


class UpdateAccount:
    def __init__(self, user_account_interface: Type[IAccountRepository]):
        self.__iuser_account = user_account_interface

    def execute(self, user_account: Type[IUserAccountRequestDto]) -> list:
        """Update user account

        Args:
            user_account (Type[IUserAccountRequestDto]): Data transfer object

        Returns:
            list: user
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

        adapter_instance.updated_at = user_account.updated_at

        if not adapter_instance.is_null_or_empty_attr():
            raise Exception("Verify empty value")

        if not user_account.account.is_valid_permition_code():
            raise Exception("Permition code is invalid")

        if not Email.is_valid_email_address(user_account.user.email):
            raise Exception("Invalid email, pleace check the email...")

        if not user_account.user.phone_number.is_valid_phone_number_of_list():
            raise Exception("Phone number is invalid")

        return self.__iuser_account.update_account(adapter_instance)
