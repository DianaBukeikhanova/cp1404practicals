CODE_LENGTH = 10


def main():
    """Manage password input and printing."""
    password = get_password("Enter a password: ")
    print_asterisks(password)


def get_password(prompt):
    """Check that password is long enough."""
    code = str(input(prompt))
    while len(code) < CODE_LENGTH:
        print("The password doesn't meet minimum length")
        code = str(input(prompt))
    return code


def print_asterisks(characters):
    """Print asterisks as long as the password."""
    for i in range(len(characters)):
        print("*", end="")


main()
