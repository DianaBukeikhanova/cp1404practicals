from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
new_guitar = Guitar("Another Guitar", 2013, 1980.24)
print(gibson)
print(gibson.get_age())
print(new_guitar.get_age())
print(gibson.is_vintage())
print(new_guitar.is_vintage())