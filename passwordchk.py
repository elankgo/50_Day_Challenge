import string

# Step 1: Take input from the user
password = input("Enter your password: ")

# Step 2: Define the conditions
has_length = len(password) > 8
has_lowercase = any(c.islower() for c in password)
special_chars = set("!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~")
has_special = any(c in special_chars for c in password)

# Step 3: Check and display result
if has_length and has_lowercase and has_special:
    print("✅ Password is valid and meets all requirements.")
else:
    print("❌ Password is invalid. Please check the following:")
    if not has_length:
        print("- It must be more than 8 characters long.")
    if not has_lowercase:
        print("- It must include at least one lowercase letter.")
    if not has_special:
        print("- It must include at least one special character.")
