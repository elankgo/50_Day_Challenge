import pyautogui

# Step 1: Ask for first number
num1 = pyautogui.prompt("Enter the first number:")

# Step 2: Ask for second number
num2 = pyautogui.prompt("Enter the second number:")

# Step 3: Convert inputs to float
try:
    a = float(num1)
    b = float(num2)

    # Step 4: Compare and show result
    if a > b:
        result = f"{a} is greater than {b}"
    elif a < b:
        result = f"{a} is smaller than {b}"
    else:
        result = "Both numbers are equal"

    pyautogui.alert(result)

except ValueError:
    pyautogui.alert("Invalid input. Please enter numeric values.")
