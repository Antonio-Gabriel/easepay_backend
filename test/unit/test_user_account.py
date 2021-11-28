from unittest import TestCase

from src.domain.entities import UserAccount, Account, User, Wallet

class TestUserAccount(TestCase):

    def test_is_null_or_empty_attr(self):
        
        account = Account(99873, 'a')
        user = User('a', 'a')
        wallet = Wallet()
        user_account = UserAccount(account, user, wallet)
        respose = user_account.is_null_or_empty_attr()

        self.assertEqual(respose, True)
