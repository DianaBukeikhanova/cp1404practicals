import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_AMOUNT = 6

quick_pick = int(input("How many quick picks? "))
for i in range(quick_pick):
    numbers = []
    for j in range(NUMBERS_AMOUNT):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(random_number)
    print(" ".join(f"{number:2}" for number in sorted(numbers)))
