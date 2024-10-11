# полиформизм Pets
# Три класса, все с различными методами "говорить"

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, ' says woof')

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, ' says meow')

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, ' says tweet')

o_dog1 = Dog('Rover')
o_dog2 = Dog('Fido')

o_cat1 = Cat('Fluffy')
o_cat2 = Cat('Spike')
o_bird = Bird('Big bird')

pets_list = [o_dog1, o_dog2, o_cat1, o_cat2, o_bird]
for o_pet in pets_list:
    o_pet.speak()

    