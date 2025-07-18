import tkinter as tk

def reverse_words():
    sentence = entry.get()
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    result = ' '.join(reversed_words)
    output_label.config(text="Reversed: " + result)
    # Store result in a variable for clipboard copy
    window.clipboard_clear()
    window.clipboard_append(result)

def clear_fields():
    entry.delete(0, tk.END)
    output_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Word Reverser")
window.geometry("450x250")

# Input label and text box
tk.Label(window, text="Enter a sentence:").pack(pady=5)
entry = tk.Entry(window, width=60)
entry.pack(pady=5)

# Reverse Button
tk.Button(window, text="Reverse Words", command=reverse_words).pack(pady=10)

# Output label
output_label = tk.Label(window, text="", fg="blue")
output_label.pack(pady=10)

# Clear and Copy buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Clear", command=clear_fields).pack(side="left", padx=10)
tk.Button(button_frame, text="Copy to Clipboard", command=lambda: window.clipboard_append(output_label.cget("text").replace("Reversed: ", ""))).pack(side="left", padx=10)

# Start the GUI loop
window.mainloop()
