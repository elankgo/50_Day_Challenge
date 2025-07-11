# Step 1: Define a list of numbers
numbers = [10, 10,10, 23, -12, 0, 99, 10]

# Step 2: Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

# Step 3: Loop through each number in the list
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Step 4: Display the results
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
