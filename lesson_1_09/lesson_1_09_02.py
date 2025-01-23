# Урок 9: Принципи SOLID в ООП.
# ➢ Принцип відкритості/закритості (Open/Closed Principle).
# Класи, модулі тощо повинні бути закриті для зміни і відкриті для розширення

from abc import ABC, abstractclassmethod

class DiscountCalculator(ABC):
    """class DiscountCalculatur"""

    @abstractclassmethod
    def get_discounted_price():
        pass

class DiscountCalculatorSilver(DiscountCalculator):
    """class DiscountCalculatorSilver"""

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        discounted_price = self.cost - (self.cost * 0.05)
        print(f"Price for User SILVER with discount 5% = {discounted_price}")
        return discounted_price
    
class DiscountCalculatorGold(DiscountCalculator):
    """class DiscountCalculatorGold"""

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        discounted_price = self.cost - (self.cost * 0.15)
        print(f"Price for User GOLD with discount 15% = {discounted_price}")
        return discounted_price
    
class DiscountCalculatorVIP(DiscountCalculator):
    """class DiscountCalculatorVIP"""

    def __init__(self, cost):
        self.cost = cost

    def get_discounted_price(self):
        discounted_price = self.cost - (self.cost * 0.3)
        print(f"Price for User V.I.P. with discount 30% = {discounted_price}")
        return discounted_price
    
user_silver_1 = DiscountCalculatorSilver(1000)
user_silver_1.get_discounted_price()

user_gold_1 = DiscountCalculatorGold(1000)
user_gold_1.get_discounted_price()

user_vip_1 = DiscountCalculatorVIP(1000)
user_vip_1.get_discounted_price()