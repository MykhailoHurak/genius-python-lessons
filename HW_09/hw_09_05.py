# Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)

# Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, 
# щоб він використовував абстракції та інтерфейси замість конкретних реалізацій. 
# Переконайтеся, що класи залежностей не знають про конкретну реалізацію інших класів.

from abc import ABC, abstractmethod

# Абстракція для сервісу доставки
class DeliveryService(ABC):
    @abstractmethod
    def deliver(self, order):
        pass

# Конкретні сервіси доставки
class NovaPost(DeliveryService):
    def deliver(self, order):
        # Логіка доставки через NovaPost
        print(f"Доставка замовлення {order} через NovaPost")

class UkrPost(DeliveryService):
    def deliver(self, order):
        # Логіка доставки через UkrPost
        print(f"Доставка замовлення {order} через UkrPost")

# Клас обробки замовлення
class OrderProcessor:
    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def process_order(self, order):
        # Логіка обробки замовлення і доставки
        self.delivery_service.deliver(order)

if __name__ == "__main__":
    # Створення замовлення
    order1 = "Замовлення #1"
    order2 = "Замовлення #2"


    # Використання NovaPost для доставки
    fedex_service = NovaPost()
    order_processor_fedex = OrderProcessor(fedex_service)
    order_processor_fedex.process_order(order1)

    # Використання UkrPost для доставки
    ups_service = UkrPost()
    order_processor_ups = OrderProcessor(ups_service)
    order_processor_ups.process_order(order2)
