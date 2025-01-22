class Counter:
    """Count of something"""

    def __init__(self, count_obj, type_obj, max_elements):
        self.count_obj = count_obj
        self. type_obj = type_obj
        self.max_elements = max_elements

    def counter(self):
        print(f"Type of object: {self.type_obj}")
        if isinstance(self.count_obj, (list, dict, str, tuple)):
            count = len(self.count_obj)
            if count > self.max_elements:
                print("Count elements of your object more than need")
                print(f"More on {count - self.max_elements}")
            else:
                print(f"Count of elements: {count}")
        else:
            print("Your object must be iterable")

    def get_attrs(self):
        print(self.__dict__)

    def set_attr(self, attr, value):
        if hasattr(self, attr):
            setattr(self, attr, value)
        else:
            print("Check your attrs")

class ListElements(Counter):
    """Class ListElements"""

    def __init__(self, count_obj, type_obj, max_elements):
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()
        print("Operation counter was ended")

    def get_attrs(self):
        super().get_attrs()
        print("Operation get_attrs was ended")

list1 = ListElements([1, 2, 3, 4, 5], list, 12)
list1.counter()
list1.get_attrs()
list1.set_attr('count_obj', [1, 2, 3, 4])
