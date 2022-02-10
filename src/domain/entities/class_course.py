from typing import Type
from decimal import Decimal

from .course import Course
from .classe import Classe


class ClassRelatedCourse:
    def __init__(self, class_id: Type[Classe], course_id: Type[Course], price: Decimal):

        self.class_id = class_id
        self.course_id = course_id
        self.price = price
