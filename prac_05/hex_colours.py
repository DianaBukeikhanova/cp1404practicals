COLOUR_TO_CODE = {"Bittersweet": "#fe6f5e", "Buff": "#f0dc82", "Cadet Blue": "#98f5ff", "Celeste": "#b2ffff",
                  "Dark Olive Green": "#caff70", "Dim Gray": "#696969", "Eggshell": "#f0ead6", "Firebrick": "#b22222",
                  "Indianred": "#ff6a6a", "Lavender Blush": "#fff0f5"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()

