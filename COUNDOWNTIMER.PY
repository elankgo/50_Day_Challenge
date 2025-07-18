import time

# Step 1: Accept the start number from the user
start = int(input("Enter the start number for countdown: "))

# Step 2: Countdown to 0 (default)
for i in range(start, -1, -1):  # From start to 0 (inclusive)
    print(i)
    time.sleep(1)  # Wait for 1 second
