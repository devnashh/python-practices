class Pets:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    
    def show_info(self):
        print(f"Pet name: {self.name}")
        print(f"Animal Type: {self.type}")
        print(f"Pet age: {self.age}")
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name} You are now {self.age}")

    
pet1 = Pets("Brownie", "Dog", 12)
pet1.birthday()
pet1.show_info()

