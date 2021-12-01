from typing import List


class PhoneNumber:
    def __init__(self, phone: List[int], id: int = None):
        self.id = id
        self.phone = phone        

    def is_valid_phone_number(self):
        """Returns true if the phone number is valid"""

        return True if (len(str(self.phone)) == 9) else False

    def is_valid_phone_number_of_list(self) -> bool:
        """Returns true if the phone number is valid"""

        for number in self.phone:
            if not len(str(number)) == 9:
                return False

        return True
