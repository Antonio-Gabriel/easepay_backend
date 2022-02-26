class Owner:
    def __init__(self, name: str, phone: str, email: str, id: int = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def is_null_or_empty_attr(self):
        """verify null or empty attribute"""

        if not (self.name != "" and self.phone != "" and self.email != ""):
            return False

        return True
