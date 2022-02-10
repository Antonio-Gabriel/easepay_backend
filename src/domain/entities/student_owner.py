from typing import Type

from .owner import Owner
from .student import Studant


class StudentOwner:
    def __init__(self, student: Type[Studant], owner: Type[Owner]):
        self.student = student
        self.owner = owner
