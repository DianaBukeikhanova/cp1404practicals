COST_BORDER = 100
DISCOUNT = 0.9

total_price = 0

items_amount = int(input("Number of items: "))
while items_amount < 0:
    print("Invalid number of items!")
    items_amount = int(input("Number of items: "))
for i in range(1, items_amount + 1):
    item_price = float(input(f"Price of item: "))
    total_price += item_price
if total_price > COST_BORDER:
    total_price *= DISCOUNT
print(f"Total price for {items_amount} items is ${total_price:.2f}")
