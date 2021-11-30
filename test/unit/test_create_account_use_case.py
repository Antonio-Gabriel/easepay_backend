from datetime import datetime
from unittest import TestCase

from src.domain.dto import IUserAccountRequestDto
from src.domain.entities import Account, User, Wallet, PhoneNumber

from src.domain.usecases import CreateAccount


class TestCreateAccountUseCase(TestCase):
    def test_create_account_use_case(self):

        create_account_usecase = CreateAccount()
        create_account_usecase.execute(
            IUserAccountRequestDto(
                account=Account(9876, "antonio"),
                user=User(
                    "António Gabriel", "antoniocampos@gmail.com", PhoneNumber(989877666)
                ),
                wallet=Wallet(),
                state=True,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        )

        self.assertTrue(True)
