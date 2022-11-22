import random

ran_num = random.randint(1, 3)


class Shooter:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def show(self):
        print(f"The name of the shooter:{self.name}", f"the age of the shooter:{self.age}",
              f"The experience of the shooter:{self.experience}")


class Beginner(Shooter):
    def __init__(self, name, age, experience):
        Shooter.__init__(self, name, age, experience)

    def shoot(self):
        if random.randint(1, 3) == 1:

            print(f"1.Beginner:\t    Probability of sticking:\t{0.01 * self.experience}:\t", True)
        else:
            print(f"1.Beginner:\t    Probability of sticking:\t{0.01 * self.experience}:\t", False)


class Experienced(Shooter):
    def __init__(self, name, age, experience):
        Shooter.__init__(self, name, age, experience)

    def shoot(self):
        if random.randint(1, 3) == 2:
            print(f"2.Experienced:\tProbability of sticking:\t{0.05 * self.experience}:\t", True)
        else:
            print(f"2.Experienced:\tProbability of sticking:\t{0.05 * self.experience}:\t", False)


class Adept(Shooter):
    def __init__(self, name, age, experience):
        Shooter.__init__(self, name, age, experience)

    def shoot(self):
        if random.randint(1, 3) == 3:
            print(f"3.Adept:\t    Probability of sticking:\t{0.9 - 0.01 * self.age}:\t", True)
        else:
            print(f"3.Adept:\t    Probability of sticking:\t{0.9 - 0.01 * self.age}:\t", False)


num1 = input("Enter the name:\t")
num2 = int(input("Enter the age:\t"))
num3 = float(input("Enter the experience:\t"))

object = Beginner(num1, num2, num3)
object1 = Experienced(num1, num2, num3)
object2 = Adept(num1, num2, num3)
object.shoot()
object1.shoot()
object2.shoot()
