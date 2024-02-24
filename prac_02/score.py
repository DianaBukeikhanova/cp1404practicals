def main():
    score = float(input("Enter score: "))
    message = evaluate_score(score)
    print(message)


def evaluate_score(estimation):
    if estimation <= 0 or estimation => 100:
        return "Invalid score"
    elif estimation >= 90:
        return "Excellent"
    elif estimation >= 50:
        return "Pass"
    else:
        return "Bad"

main()