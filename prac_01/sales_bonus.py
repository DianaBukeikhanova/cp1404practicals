"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_STANDARD = 1000
sale = float(input("Enter sales: $"))
while sale >= 0:
    if sale >= SALES_STANDARD:
        bonus_percentage = 0.15
    else:
        bonus_percentage = 0.1
    final_bonus = sale * bonus_percentage
    print(f"Your bonus is {bonus_percentage} and final sale is {final_bonus}")
    sale = float(input("Enter sales: $"))
