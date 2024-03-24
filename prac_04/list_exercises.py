# 1 task
FIRST_ATTEMPT = 1
LAST_ATTEMPT = 6

numbers = []

for i in range(FIRST_ATTEMPT, LAST_ATTEMPT):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


# 2 task
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = str(input("Enter username: "))
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")
