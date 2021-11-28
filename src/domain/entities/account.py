from ..validator import PasswordHash

class Account:
    def __init__(self, permition_code: int, password: str):
        self.permition_code = permition_code
        self.password = password
    
    def password_encrypt(self) -> bytes:
        """ Enctrypt password """

        return PasswordHash.Enctrypt(self.password)
    
    def password_verify(self, comparison_pass: bytes) -> bool:
        """ Verify if password is valid or not """

        return PasswordHash.isValidPassword(self.password, comparison_pass)