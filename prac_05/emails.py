"""
Emails
Estimate: 35 minutes
Actual:   38  minutes
"""


def main():
    """Based on email show name and email."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = separate_name_from_email(email)
        name = check_name(full_name)
        email_to_name[email] = name
        email = input("Email: ")
    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


def check_name(full_name):
    """Check found name is correct."""
    answer = input(f"Is your name {full_name}? (Y/n) ").upper()
    if "N" in answer:
        name = input("Name: ")
        return name
    return full_name


def separate_name_from_email(email):
    """Separate name from email to find name."""
    parts = email.split("@")
    name_details = parts[0].split(".")
    full_name = " ".join(name_details).title()
    return full_name


main()