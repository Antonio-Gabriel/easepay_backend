from unittest import TestCase

from src.domain.entities import Account

class TestHashPassword(TestCase):            

    def test_hash_password(self):

        account = Account(99873, 'antonio')
        #literal_password = account.password_encrypt()

        current_pass = b'7bd609ad1b5a0c4a52c012263801539c1235cf4f'
        response = account.password_verify(current_pass)
        self.assertTrue(response, True)

    def test_is_valid_permition_code(self):
        
        account = Account(9987, 'antonio')
        response = account.is_valid_permition_code()
        
        self.assertTrue(response, True)