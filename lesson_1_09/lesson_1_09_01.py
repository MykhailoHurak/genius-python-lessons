# Урок 9: Принципи SOLID в ООП.
# ➢ Принцип єдиного обов'язку (Single Responsibility Principle).
# Один клас відповідає за роботу одного методу

class Journal:
    """class Journal - для створення заміток"""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
    
    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return "\n".join(self.entries)
        
class SaveFiles:
    """class SaveFiles - для збереження файлів"""

    @staticmethod
    def save_to_file(journal, filename):
        with open(file=filename, mode="w") as file:
            file.write(journal)

class LoadFrowWeb:
    """class LoadFrowWeb - для завантаження з Web"""

    @staticmethod
    def load(journal, filename):
        pass    


    
journal1 = Journal()
journal1.add_entry("I ate today")
journal1.add_entry("I slepr yesterday")
print(f"Count of entries:\n{journal1}")