# Інкапсуляція

class Card:
    """class Card"""

    def __init__(self, card_number, balance):
        if self.__check_attribute_type(card_number, str):
            self._card_number = card_number
        if self.__check_attribute_type(balance, float):
            self.__balance = balance

    def get_card_data(self):
        return self.__dict__
    
    def set_card_data(self, attr, value):
        if self.__check_attribute_type(attr, str):
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return "Attribute must be string type"

    def __check_attribute_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be {should_be}")

user1 = Card('4141 0000 1111 2222', 1555.0)
print(user1.get_card_data())
print(user1.set_card_data("card_number", "4141 5555 6666 7777"))
print(user1.set_card_data("balance", 2222.0))
print(user1.get_card_data())