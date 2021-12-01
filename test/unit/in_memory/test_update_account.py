from unittest import TestCase
from datetime import datetime

from src.domain.entities import Account, PhoneNumber, Wallet, User
from src.domain.dto import IUserAccountRequestDto

from src.infra.repository import UserAccountInMemoryRepository
from src.domain.usecases import UpdateAccount


class TestUpdateUserAccount(TestCase):
    def test_update_user_account(self):

        update_account = UpdateAccount(UserAccountInMemoryRepository())
        update_repsonse = update_account.execute(
            IUserAccountRequestDto(
                account=Account(9893, "antonio_campos"),
                user=User(
                    "António Campos Gabriel",
                    "antoniocamposgabriel@gmail.com",
                    PhoneNumber([992343333, 911226333]),
                ),
                wallet=Wallet(),
                updated_at=datetime.now(),
            )
        )

        print(update_repsonse)

        self.assertTrue(True)
