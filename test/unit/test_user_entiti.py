from unittest import TestCase

from src.domain.entities import User

class TestUserEntiti(TestCase):
    
    def test_is_valid_email_address(self):

        user = User('António', 'antonio@gmail.com.pt')
        response = user.is_valid_email_address()

        self.assertEqual(response, True)