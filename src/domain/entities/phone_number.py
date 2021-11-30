from typing import List


class PhoneNumber:
    def __init__(self, phone: List[int], id: int = None):
        self.id = id
        self.phone = phone

        self.__contant_list = []

    def insert_multiple_contact(self, *args):
        """Insert multiple contact"""

        self.__contant_list.append(*args)

    def return_contacts(self):
        """Return a list"""

        return self.__contant_list[0]

    def is_valid_phone_number(self):
        """Returns true if the phone number is valid"""

        return True if (len(str(self.phone)) == 9) else False

    def is_valid_phone_number_of_list(self) -> bool:
        """Returns true if the phone number is valid"""

        for number in self.__contant_list:
            for phone in number:
                if not len(str(phone)) == 9:
                    return False

        return True
