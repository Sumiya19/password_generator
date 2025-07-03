import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    char_set = ''
    length = int(length_var.get())

    if digits_var.get():
        char_set += string.digits
    if uppercase_var.get():
        char_set += string.ascii_uppercase
    if lowercase_var.get():
        char_set += string.ascii_lowercase
    if special_var.get():
        char_set += "!@#$%^&*()-_=+[{]}|;:,<.>/?"

    if not char_set:
        password_display.config(text="Select at least one option!", fg="red")
        copy_btn.config(state="disabled")
        return

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_display.config(text=password, fg="black")
    copy_btn.config(state="normal")
    copied_label.config(text="")  # Clear tooltip on regenerate

def copy_password():
    password = password_display.cget("text")
    if password and "Select at least one" not in password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copied_label.config(text="✔ Copied to clipboard!", fg="green")

# Main GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x440")
root.configure(bg="#f5f6fa")

tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 20, "bold"), bg="#f5f6fa", fg="#2f3640").pack(pady=20)

# Dropdown section
frame = tk.Frame(root, bg="#dcdde1", bd=2, relief="groove")
frame.pack(pady=10, padx=30)

tk.Label(frame, text="Select Character Types:", font=("Arial", 12), bg="#dcdde1").pack(pady=10)

digits_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(frame, text="Digits (0-9)", variable=digits_var, bg="#dcdde1").pack(anchor='w', padx=20)
tk.Checkbutton(frame, text="Uppercase Letters (A-Z)", variable=uppercase_var, bg="#dcdde1").pack(anchor='w', padx=20)
tk.Checkbutton(frame, text="Lowercase Letters (a-z)", variable=lowercase_var, bg="#dcdde1").pack(anchor='w', padx=20)
tk.Checkbutton(frame, text="Special Characters (!@#...)", variable=special_var, bg="#dcdde1").pack(anchor='w', padx=20)

# Password Length
length_frame = tk.Frame(root, bg="#f5f6fa")
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f5f6fa").pack(side="left")
length_var = tk.StringVar(value="12")
tk.Entry(length_frame, textvariable=length_var, width=5, font=("Arial", 12)).pack(side="left", padx=10)

# Generate button
tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#44bd32", fg="white", padx=10, pady=5, command=generate_password).pack(pady=15)

# Display area
password_display = tk.Label(root, text="Your password will appear here", font=("Arial", 14, "bold"), bg="#f5f6fa")
password_display.pack(pady=10)

# Copy button + Copied status
copy_btn = tk.Button(root, text="📋 Copy", font=("Arial", 12), bg="#0984e3", fg="white", command=copy_password)
copy_btn.pack(pady=5)
copy_btn.config(state="disabled")

copied_label = tk.Label(root, text="", font=("Arial", 10), bg="#f5f6fa")
copied_label.pack()

# Start GUI
root.mainloop()