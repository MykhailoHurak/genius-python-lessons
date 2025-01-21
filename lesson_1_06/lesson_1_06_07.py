class FootballPlayer:
    """Class for create fottball players"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def get_attributes(self):
        print(self.__dict__)
        print(f"Name: {self.name}, Country: {self.country}")

    def set_attributes(self, name, country):
        self.name = name
        self.country = country
        print(f"new Name: {self.name}, new Country: {self.country}")

player1 = FootballPlayer('Cristiano', 'Portugal')

player1.get_attributes()
player1.set_attributes('Cristiano Ronaldo', 'Ukraine')