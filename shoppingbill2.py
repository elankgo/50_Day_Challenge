# Program to input 3 items and display a formatted bill with 18% tax

TAX_RATE = 0.18  # 18%
items = []

# Input 3 items
for i in range(1, 4):
    name = input(f"Enter name of item {i}: ")
    price = float(input(f"Enter price of {name}: ₹"))
    tax = price * TAX_RATE
    total = price + tax
    items.append((name, price, tax, total))

# Display formatted bill
print("\n" + "="*50)
print("{:<20} {:>10} {:>10} {:>10}".format("Item", "Price", "Tax(18%)", "Total"))
print("-"*50)

grand_total = 0
for name, price, tax, total in items:
    print("{:<20} {:>10.2f} {:>10.2f} {:>10.2f}".format(name, price, tax, total))
    grand_total += total

print("-"*50)
print("{:<20} {:>10} {:>10} {:>10.2f}".format("TOTAL", "", "", grand_total))
print("="*50)
