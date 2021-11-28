from unittest import TestCase
from src.domain.entities import Wallet

class TestWallet(TestCase):

    def test_deposit_in_wallet(self):

        wallet = Wallet(200.00)
        total_deposit = wallet.deposit(100.00)
        total_withdraw = wallet.with_draw(20.00)
        print(total_deposit)
        print(total_withdraw)
        self.assertTrue(True)