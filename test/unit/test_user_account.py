from unittest import TestCase

from src.domain.entities import UserAccount, Account, User, Wallet, PhoneNumber


class TestUserAccount(TestCase):
    def test_is_null_or_empty_attr(self):

        phone_number = PhoneNumber(9)
        account = Account(99873, "a")
        user = User("a", "a", phone_number)
        wallet = Wallet()
        user_account = UserAccount(account, user, wallet)
        respose = user_account.is_null_or_empty_attr()

        self.assertEqual(respose, True)
