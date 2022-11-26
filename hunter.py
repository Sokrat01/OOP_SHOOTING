import random


class Shooter:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def show(self):
        print(f"Name of shooter {self.name}", f"age {self.age}", f"experience {self.experience}")


class Beginner(Shooter):

    def __init__(self, name, age, experience):
        super().__init__(name, age, experience)

    def shoot(self):
        print(f"1. Beginner: Result of shoot:{0.01 * self.experience}:")

        if random.randint(1, 3) == 1:
            return True
        else:
            return False


class Middle(Shooter):

    def __init__(self, name, age, experience):
        super().__init__(name, age, experience)

    def shoot(self):
        print(f"2. Middle: Result of shoot {0.05 * self.experience}")

        if random.randint(1, 3) == 2:
            return True
        else:
            return False


class Professional(Shooter):

    def __init__(self, name, age, experience):
        super().__init__(name, age, experience)

    def shoot(self):
        print(f"3. Professional: Result of shoot{0.09 * self.experience}:")

        if random.randint(1, 3) == 3:
            return True
        else:
            return False


shooter = Shooter("Mika", 30, 5)
shooter.show()
beginner = Beginner(input("Name of beginner hunter:\t"), int(input("age\t")), float(input("experience\t")))
print(beginner.shoot())
middle = Middle(input("Name of middle hunter:\t"), int(input("age\t")), float(input("experience\t")))
print(middle.shoot())
professional = Professional(input("Name of professional hunter:\t"), int(input("age\t")), float(input("experience\t")))
print(professional.shoot())
