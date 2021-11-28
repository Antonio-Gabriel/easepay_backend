from unittest import TestCase

from src.domain.entities import User, PhoneNumber

class TestUserEntiti(TestCase):
    
    def test_is_valid_email_address(self):

        user = User('António', 'antonio@gmail.com.pt')
        response = user.is_valid_email_address()

        self.assertEqual(response, True)

    def test_valid_phone_number(self):

        phone_number = PhoneNumber(998987888, 1)
        response = phone_number.is_valid_phone_number()

        self.assertEqual(response, True)
    
    def test_insert_multiple_contacts(self):

        phone_number = PhoneNumber(998987888, 1)
        contact_lists = [phone_number.phone, 998988348, 982344392]
        phone_number.insert_multiple_contact(contact_lists)
        response = phone_number.is_valid_phone_number_of_list()

        print(phone_number.return_contacts())
        self.assertEqual(response, True)