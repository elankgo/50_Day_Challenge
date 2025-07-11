# Step 1: Take input from the user
n = int(input("Enter a positive integer (n): "))

# Step 2: Initialize the sum variable
total = 0

# Step 3: Use a loop to add numbers from 1 to n
for i in range(1, n + 1):
    total += i  # Add i to total

# Step 4: Display the result
print(f"The sum of numbers from 1 to {n} is: {total}")