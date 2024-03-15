"""
Wimbledon
Estimate: 45 minutes
Actual:   53 minutes
"""
FILE_NAME = "wimbledon.csv"


def main():
    """Display all information about champions."""
    details = convert_data(FILE_NAME)
    champion_to_amount, countries = analyse_material(details)

    print("Wimbledon Champions: ")
    print('\n'.join([f"{champion:16}: {wins_count}" for champion, wins_count in champion_to_amount.items()]))
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def convert_data(filename):
    """Convert text to list of information."""
    details = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file.readlines()[1:]:
            material = line.strip().split(",")
            details.append(material)
    return details


def analyse_material(details):
    """Analyse and prepare countries and wins."""
    countries = set()
    champion_to_amount = {}

    for data in details:
        try:
            champion_to_amount[data[2]] += 1
        except KeyError:
            champion_to_amount[data[2]] = 1
        countries.add(data[1])
    return champion_to_amount, countries


main()
