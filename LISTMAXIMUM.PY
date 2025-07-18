# Step 1: Accept a list of numbers as input
numbers = input("Enter numbers separated by spaces: ")

# Step 2: Convert the input string into a list of integers
num_list = [int(num) for num in numbers.split()]

# Step 3: Initialize the largest variable with the first element
largest = num_list[0]

# Step 4: Loop through the list to find the largest number
for num in num_list:
    if num > largest:
        largest = num

# Step 5: Display the result
print("The largest number is:", largest)
