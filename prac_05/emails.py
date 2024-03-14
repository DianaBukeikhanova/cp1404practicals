"""
Emails
Estimate: 35 minutes
Actual:   38  minutes
"""
email_to_name = {}

email = input("Email: ")

while email != "":
    # Separate email into full name and email's configuration
    parts = email.split("@")

    # Split name into first and second names
    name_details = parts[0].split(".")

    # Make full name by joining and titling each part of full name
    full_name = " ".join(name_details).title()

    # Provide key and value into dictionary
    email_to_name[email] = full_name
    answer = input(f"Is your name {full_name}? (Y/n) ").upper()
    # LBYL and EAFP
    if "N" in answer:
        name = input("Name: ")
    email = input("Email: ")

print()

# Print all from dictionary
for email in email_to_name:
    print(f"{email_to_name[email]} ({email})")
