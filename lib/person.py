class Person:
    # Constructor (initializer) method
    def __init__(self, name):
        self.name = name

    # Instance method to talk
    def talk(self):
        print(f"{self.name} says Hello World!")

    # Instance method to walk
    def walk(self):
        print(f"{self.name} is walking.")
