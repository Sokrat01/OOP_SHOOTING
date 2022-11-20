# Exercise 1 Create a parent class Animal and child classes(Monkey, Donkey) and use polymorphism with inheritance

class Animal:
    pet_animal = "donkey"
    wild_animal = "monkey"

    def type_of_animals(self):
        return self.pet_animal, self.wild_animal


class Monkey(Animal):

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


class Donkey(Animal):

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


a = Animal()
m = Monkey("orange", "50 lbs")
d = Donkey("gray", "300 lbs")
print("Type of animal", a.wild_animal, "color", m.color, "weight", m.weight)
print("Type of animal", a.pet_animal, "color", d.color, "weight", d.weight)
print(" ")


# Exercise 2 Create a base class Car and child classes (BMW, Ferrari) and get max_speed method from base class and
# also child classes should have custom method


class Car:
    speed = 260
    speed2 = 340

    def max_speed(self):
        pass


class BMW(Car):
    color = "black"
    type = "sedan"

    def car(self):
        return f"About Bmw: Color is {self.color}, type of {self.type}:"

    def speed_of_car(self):
        return f"Max speed is {self.speed}"

    def info(self):
        return "BMW was created in 1917 from the Munich firm Rapp-Motorenwerke:"


class Ferrari(Car):
    color = "red"
    type = "supercar"

    def car(self):
        return f"About Ferrari: Color is {self.color}, type of {self.type}:"

    def speed_of_car(self):
        return f"Max speed is {self.speed2}"

    def info(self):
        return "Ferrari is an Italian luxury sports car manufacturer based in Maranello, Italy Founded by Enzo Ferrari (1898–1988)"


b = BMW()
f = Ferrari()
print(b.car())
print(b.info(), b.speed_of_car())
print(f.car(), f.speed_of_car())
print(f.info())












