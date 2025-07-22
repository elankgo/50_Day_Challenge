# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Extract initial
initial = first_name[0].upper()

# Display result
print("Your name is:", initial + ".", last_name.title())
