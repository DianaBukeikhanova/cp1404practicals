"""
Guitars
Estimate: 45 minutes
Actual: 55 minutes
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ").title()
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    print(Guitar(name, year, cost), "added.")
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ").title()

print("These are my guitars:")
# for i in range(len(guitars)):
#     print(f"Guitar {i + 1}: {guitars[i]}")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    # if guitar.is_vintage():
    #     vintage_string = "(vintage)"
    # else:
    #     vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
