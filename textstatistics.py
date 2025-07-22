import tkinter as tk
import re

def analyze_paragraph():
    text = text_input.get("1.0", tk.END).strip()

    char_count = len(text)
    word_count = len(text.split())
    sentence_count = len([s for s in re.split(r'[.!?]+', text) if s.strip()])

    result = (
        f"Characters: {char_count}\n"
        f"Words: {word_count}\n"
        f"Sentences: {sentence_count}"
    )

    result_label.config(text=result)

# Create main window
window = tk.Tk()
window.title("Paragraph Analyzer")
window.geometry("500x400")

# Widgets
tk.Label(window, text="Enter your paragraph below:", font=("Arial", 12)).pack(pady=10)

text_input = tk.Text(window, height=10, width=60)
text_input.pack(pady=5)

tk.Button(window, text="Analyze", command=analyze_paragraph).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue", justify="left")
result_label.pack(pady=10)

# Start GUI loop
window.mainloop()
