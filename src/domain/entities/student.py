from typing import Type

from .class_course import ClassRelatedCourse


class Studant:
    def __init__(
        self,
        name: str,
        process: int,
        email: str,
        phone: int,
        district: str,
        location: str,
        avatar: str,
        class_course: Type[ClassRelatedCourse],
        state: bool = True,
        id: int = None,
    ):
        self.id = id
        self.name = name
        self.process = process
        self.email = email
        self.phone = phone
        self.district = district
        self.location = location
        self.avatar = avatar
        self.class_course = class_course
        self.state = state
