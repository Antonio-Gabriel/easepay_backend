from datetime import datetime


class Course:
    def __init__(
        self,
        name: str,
        state: bool,
        created_at: datetime,
        updated_at: datetime,
        id: int = None,
    ):
        self.id = id
        self.name = name
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
