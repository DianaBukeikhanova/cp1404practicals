MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input("").lower()
while choice != "q":
    if choice == "h":
        print(f'Hello {name}')
    elif choice == "g":
        print(f'Goodbye {name}')
    else:
        print("Invalid choice")
    print(MENU)
    choice = input().lower()
print("Finished.")
