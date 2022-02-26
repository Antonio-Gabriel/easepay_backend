from typing import Type

from ...enums import Size
from ..payment import Payment
from ..student import Studant
from .uniform_type import UniformType


class UniformPayment:
    def __init__(
        self,
        size: Type[Size],
        payment: Type[Payment],
        student: Type[Studant],
        uniform_type: Type[UniformType],
    ):
        self.size = size
        self.payment = payment
        self.student = student
        self.uniform_type = uniform_type
