from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    prepare_guitars_details(guitars, in_file)
    in_file.close()
    display_sorted_guitars(guitars)


def prepare_guitars_details(guitars, in_file):
    in_file.readline()
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
