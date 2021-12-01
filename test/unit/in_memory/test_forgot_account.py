from unittest import TestCase

from src.domain.usecases import ForgotUserAccount
from src.infra.repository import UserAccountInMemoryRepository


class TestForgotAccount(TestCase):
    def test_forgot_account(self):

        forgot_account = ForgotUserAccount(UserAccountInMemoryRepository())
        user_account = forgot_account.execute('antoniogabriel@gmail.com')        

        print(user_account)
        self.assertIsInstance(user_account, list)
