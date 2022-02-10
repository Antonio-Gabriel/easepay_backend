from ..domain.entities import (
    StudentAccount,
    Studant,
    Account,
    Wallet,
    PhoneNumber,
    PriceOfClass,
)


class StudantAccountAdapter:
    @staticmethod
    def create(
        name: str,
        email: str,
        district: str,
        location: str,
        residence_number: int,
        permition_code: int,
        password: str,
    ):

        return StudentAccount(
            account=Account(permition_code, password), student=Studant()
        )
