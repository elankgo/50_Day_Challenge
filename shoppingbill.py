# Program to input 3 items with price, calculate 18% tax, and display item-wise + total bill

TAX_RATE = 0.18  # 18%

items = []  # List to store item details

# Input 3 items
for i in range(1, 4):
    name = input(f"Enter name of item {i}: ")
    price = float(input(f"Enter price of {name}: ₹"))
    tax = price * TAX_RATE
    total = price + tax
    items.append((name, price, tax, total))

# Display bill
print("\n----- BILL DETAILS -----")
grand_total = 0
for name, price, tax, total in items:
    print(f"Item: {name}")
    print(f"  Price: ₹{price:.2f}")
    print(f"  Tax (18%): ₹{tax:.2f}")
    print(f"  Total: ₹{total:.2f}\n")
    grand_total += total

print(f"Total Bill Amount: ₹{grand_total:.2f}")
