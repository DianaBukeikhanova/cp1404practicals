HIGHEST_SCORE_BORDER = 100
LOWEST_SCORE_BORDER = 0
EXCELLENT_BORDER = 90
PASS_SCORE_BORDER = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Print menu and handle options based on user's choice."""
    print(MENU)
    choice = str(input(">>> ")).upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter your score(0-100): ")
        elif choice == "P":
            print(f"{score} is {evaluate_score(score)} score.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = str(input(">>> ")).upper()
    print("Farewell.")


def get_valid_score(prompt):
    """Get valid score."""
    score = int(input(prompt))
    while score < LOWEST_SCORE_BORDER or score > HIGHEST_SCORE_BORDER:
        print("Invalid score.")
        score = int(input(prompt))
    return score


def evaluate_score(score):
    """Evaluate score's category."""
    if score >= EXCELLENT_BORDER:
        return "Excellent"
    elif score >= PASS_SCORE_BORDER:
        return "Pass"
    else:
        return "Bad"


def print_stars(number):
    """Print as many stars as the score."""
    for i in range(number):
        print("*", end="")


main()
