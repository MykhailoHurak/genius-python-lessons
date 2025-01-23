# Урок 9: Принципи SOLID в ООП.
# ➢ Принцип розділення інтерфейсу (Interface Segregation Principle).
# Клієнти не повинні залежати від інтерфейсів, які вони не використовують

from abc import ABC, abstractclassmethod

class MakeCall(ABC):
    """class MakeCall"""

    @abstractclassmethod
    def make_call(self):
        pass

class SendSms(ABC):
    """class SendSms"""

    @abstractclassmethod
    def send_sms(self):
        pass

class GetInternet(ABC):
    """class GetInternet"""

    @abstractclassmethod
    def get_internet(self):
        pass

class MobilePhone(MakeCall, SendSms, GetInternet):
    """class MobilePhone"""

    def make_call(self):
        print("Calling to abonent...") 

    def send_sms(self):
        print("Sending SMS to abonent...")

    def get_internet(self):
        print("Getting Internet...")

class StacionarPhone(MakeCall):
    """class StacionarPhone"""

    def make_call(self):
        print("Calling to abonent...") 

mobile_phone_1 = MobilePhone()
mobile_phone_1.make_call()
mobile_phone_1.send_sms()
mobile_phone_1.get_internet()

print("-------")

stacionar_phone_1 = StacionarPhone()
stacionar_phone_1.make_call()