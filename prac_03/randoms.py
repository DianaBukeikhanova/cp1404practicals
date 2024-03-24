import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?       14
# What was the smallest number you could have seen, what was the largest?       Smallest - 5, Largest - 20

# What did you see on line 2?       9
# What was the smallest number you could have seen, what was the largest?       Smallest - 3, Largest - 9
# Could line 2 have produced a 4?   No

# What did you see on line 3?       float number with 16 numbers after dot (2.6553903124203924)
# What was the smallest number you could have seen, what was the largest?       Smallest - 2.5, Largest - 5.5

print(random.randint(1, 100))  # line 4
