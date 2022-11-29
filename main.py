from Beginner import *
from Experienced import *
from Skilled_hunter import *

beginner = Beginner(input("Name of beginner hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(beginner.shoot())
experienced = Experienced(input("Name of experienced hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(experienced.shoot())
skilled_hunter = SkilledHunter(input("Name of professional hunter\t"), int(input("Age\t")), float(input("Experience\t")))
print(skilled_hunter.shoot())


def shoot_result():
    for give_only_True in (beginner, experienced, skilled_hunter):
        file = open("Shooting_result_log.txt", "a", encoding="utf = 8")
        file.write(give_only_True.show())
        if give_only_True is True:
            file.write(f"The {True} result {give_only_True}\n")
        else:
            file.write(f"The {False} result {give_only_True}\n")
        file.close()


shoot_result()

