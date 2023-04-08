class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display(self):
        print(f"{self.name} is a {self.species}")


class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name, species="dog")
        self.breed=breed

    def display(self):
        super().display()
        print(f"{self.name} is a {self.breed} {self.species}")

dog=Dog("Buddy","Golden Retriever")
dog.display()