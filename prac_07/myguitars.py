from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    prepare_guitars_details(guitars, in_file)
    guitars = enter_new_guitar(guitars)
    write_guitars_to_file(guitars)
    display_sorted_guitars(guitars)
    in_file.close()


def write_guitars_to_file(guitars):
    """Write all new guitars inside the file in special format."""
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def enter_new_guitar(guitars):
    """Add new entered guitars inside list."""
    print("My guitars!")
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(Guitar(name, year, cost), "added.")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").title()
    return guitars


def prepare_guitars_details(guitars, in_file):
    """Process the data and prepare to display."""
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the language we've just constructed to the list
        guitars.append(guitar)


def display_sorted_guitars(guitars):
    """Loop through and display all languages (using their str method)."""
    guitars.sort().__lt__(1)
    for guitar in guitars:
        print(guitar)


main()
