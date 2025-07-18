import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        name = name_entry.get()
        marks = []
        for entry in mark_entries:
            val = float(entry.get())
            if val < 0 or val > 100:
                messagebox.showerror("Error", "Marks must be between 0 and 100")
                return
            marks.append(val)

        # Check pass/fail
        passed = all(mark >= 50 for mark in marks)
        total = sum(marks)
        average = total / 5

        # Grade logic
        if average > 90:
            grade = "Outstanding"
        elif average > 80:
            grade = "Very Good"
        elif average > 60:
            grade = "Good"
        else:
            grade = "Needs Improvement"

        result = f"Name: {name}\nTotal: {total}/500\nAverage: {average:.2f}%\nStatus: {'PASS ✅' if passed else 'FAIL ❌'}\nGrade: {grade if passed else 'N/A'}"
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric marks")

# Setup main window
window = tk.Tk()
window.title("Student Result Calculator")
window.geometry("400x400")

# Widgets
tk.Label(window, text="Enter Student Name:").pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

subjects = ["Maths", "Science", "Physics", "English", "Biology"]
mark_entries = []

for subject in subjects:
    tk.Label(window, text=f"{subject} Marks (0-100):").pack()
    entry = tk.Entry(window, width=10)
    entry.pack(pady=2)
    mark_entries.append(entry)

tk.Button(window, text="Calculate Result", command=calculate_result).pack(pady=10)

result_label = tk.Label(window, text="", fg="blue", font=("Arial", 10), justify="left")
result_label.pack(pady=10)

window.mainloop()
