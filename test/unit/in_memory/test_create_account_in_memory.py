from datetime import datetime
from unittest import TestCase
from src.domain.entities.phone_number import PhoneNumber
from src.domain.entities.user import User
from src.domain.entities.wallet import Wallet
from src.domain.entities import Account
from src.domain.dto.user_account_dto import IUserAccountRequestDto
from src.infra.repository.user_account_in_memory import UserAccountInMemoryRepository

from src.domain.usecases import CreateAccount


class TestCreateAccountInMemory(TestCase):
    def test_create_account_in_memory(self):

        create_account = CreateAccount(UserAccountInMemoryRepository())
        create_account.execute(
            IUserAccountRequestDto(
                account=Account(9872, "antonio"),
                user=User(
                    "António Gabriel", "exemplo@gmail.com", PhoneNumber(989877666)
                ),
                state=True,
                wallet=Wallet(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
        )

        self.assertTrue(True)
