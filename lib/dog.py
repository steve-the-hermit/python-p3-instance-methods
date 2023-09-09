class Dog:
    # Constructor (initializer) method
    def __init__(self, name):
        self.name = name

    # Instance method to bark
    def bark(self):
        print(f"{self.name} says Woof!")

    # Instance method to sit
    def sit(self):
        print(f"{self.name} is sitting.")
