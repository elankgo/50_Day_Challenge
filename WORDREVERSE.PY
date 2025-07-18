# Step 1: Take input from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Reverse each word using slicing
reversed_words = [word[::-1] for word in words]

# Step 4: Join the reversed words back into a sentence
result = ' '.join(reversed_words)

# Step 5: Print the result
print("Reversed words sentence:", result)