# Program to check if a number is odd or even

# Step 1: Get input from the user
num = int(input("Enter a number: "))

# Step 2: Use modulus operator to check
if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
