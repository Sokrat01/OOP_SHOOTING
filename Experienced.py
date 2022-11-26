from Shooter import *
import random


class Experienced(Shooter):

    def __init__(self, name, age, experience):
        super().__init__("Experienced", name, age, experience)

    def shoot(self):
        hit_probability = 0.05 * self._experience
        print(f"hit probability:\t {hit_probability}")

        random_number = random.uniform(0.01, 2)
        print(f"random number:\t {random_number}")

        shoot_result = random_number <= hit_probability
        print(f"2. Middle: Result of shoot {shoot_result}")

        result = True if shoot_result else False
        return result