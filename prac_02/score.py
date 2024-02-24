import random


def main():
    """Based on score, print score's category."""
    user_score = float(input("Enter score: "))
    print(evaluate_score(user_score))

    random_score = random.randint(0, 100)
    print(f"Your random score: {random_score}\n"
          f"It is {evaluate_score(random_score)}.")



def evaluate_score(score):
    """Evaluate score's category."""
    if score <= 0 or score >= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
