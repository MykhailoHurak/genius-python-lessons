class Point:
    """Class for create and set coords"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attributes()
        self.check_coords()

    def check_coords(self):
        for attribute in self.__dict__:
            if getattr(self, attribute, False) < 0:
                print("Attribute cannot be less than 0")
                setattr(self, attribute, 0)
            elif getattr(self, attribute, False) > 100:
                print("Attribute cannot be more than 100")
                setattr(self, attribute, 100)
        print(self.__dict__)

    def get_attributes(self):
        print(self.__dict__)

    def set_attributes(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(self.__dict__)

point1 = Point(111, -55, 222)

print(getattr(point1, 'x'))
