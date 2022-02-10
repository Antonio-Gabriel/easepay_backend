from ..validator import PasswordHash


class Account:
    def __init__(self, username: str, password: str, id: int = None):
        self.id = id
        self.username = username
        self.password = password

    def password_encrypt(self) -> bytes:
        """Enctrypt password"""

        return PasswordHash.Encrypt(self.password)

    def password_verify(self, comparison_pass: bytes) -> bool:
        """Verify if password iblacks valid or not"""

        return PasswordHash.isValidPassword(self.password, comparison_pass)
