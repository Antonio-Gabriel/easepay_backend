from typing import Type
from ...enums import Months
from ..payment import Payment
from ..student import Studant


class MonthlyPayment:
    def __init__(
        self, month: Type[Months], payment: Type[Payment], student: Type[Studant]
    ):
        self.month = month
        self.payment = payment
        self.student = student
