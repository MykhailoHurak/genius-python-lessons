class BaseInterface:
    """Class BaseInterface"""

    def __init__(self) -> None:
        pass

    def get_attrs(self) -> None:
        pass

    def print_mode(self) -> None:
        pass

    def count_of_price(self) -> None:
        pass

    def call_to_support(self) -> None:
        pass

class InterfaceOfSite(BaseInterface):
    """Class InterfaceOfSite"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_mode(self) -> None:
        print(f"Model of site: {self.model}")

    def count_of_price(self) -> None:
        print(f"Count of site price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support is {self.number}")
        print(f"You can call from 8am to 19am")

class InterfaceOfApp(BaseInterface):
    """Class InterfaceOfApp"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_mode(self) -> None:
        print(f"Model of application: {self.model}")

    def count_of_price(self) -> None:
        print(f"Count of application price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support i2 {self.number}")
        print(f"You can call from 8am to 19am")

user_site = InterfaceOfSite(111, "shop", 500)
user_app = InterfaceOfApp(444, "android", 2500)

user_site.print_mode()
user_site.count_of_price()
user_site.call_to_support()

print("-------")

user_app.print_mode()
user_app.count_of_price()
user_app.call_to_support()