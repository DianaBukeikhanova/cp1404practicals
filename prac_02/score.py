HIGHEST_SCORE = 100
LOWEST_SCORE = 0
EXCELLENT_BORDER = 90
PASS_SCORE_BORDER = 50

import random


def main():
    """Based on score, print score's category."""
    user_score = float(input("Enter score: "))
    print(evaluate_score(user_score))
    random_score = random.randint(LOWEST_SCORE, HIGHEST_SCORE)
    print(f"Your random score: {random_score}\n"
          f"It is {evaluate_score(random_score)}.")


def evaluate_score(score):
    """Evaluate score's category."""
    if score <= LOWEST_SCORE or score >= HIGHEST_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_BORDER:
        return "Excellent"
    elif score >= PASS_SCORE_BORDER:
        return "Pass"
    else:
        return "Bad"


main()
