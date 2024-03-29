NAMES_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

# 1.
name = input("Name: ")
out_file = open(name, "w")
out_file.write(name)
out_file.close()

# 2.
in_file = open(NAMES_FILE)
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

# 3.
with open(NUMBERS_FILE, "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
result = first_number + second_number
print(result)

# 4.
with open(NUMBERS_FILE, "r") as in_file:
    total = 0
    for number in in_file:
        total += int(number)
    print(f"Total sum is {total}")

