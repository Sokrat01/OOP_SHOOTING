from Shooter import *
import random


class SkilledHunter(Shooter):

    def __init__(self, name, age, experience):
        super().__init__("Skilled hunter's", name, age, experience)

    def shoot(self):
        hit_probability = 0.9 - 0.01 * self._age
        print(f"hit probability {hit_probability}")

        random_number = random.uniform(0.01, 3)
        print(f"random number {random_number}")

        shoot_result = random_number <= hit_probability
        print(f"3. Professional: Result of shoot {shoot_result}")

        result = True if shoot_result else False
        return result
