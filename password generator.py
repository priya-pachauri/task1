import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Password length
        tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        self.length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
        self.length_entry.pack()

        # Options
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper, bg="#f0f0f0").pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lower, bg="#f0f0f0").pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits, bg="#f0f0f0").pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols, bg="#f0f0f0").pack(anchor="w", padx=20)

        # Generate button
        tk.Button(root, text="Generate Password", command=self.generate_password, bg="#007acc", fg="white", font=("Arial", 12)).pack(pady=15)

        # Output field
        self.password_output = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
        self.password_output.pack(pady=10)

        # Copy button
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#4caf50", fg="white", font=("Arial", 12)).pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                raise ValueError("Password too short")

            characters = ""
            if self.include_upper.get():
                characters += string.ascii_uppercase
            if self.include_lower.get():
                characters += string.ascii_lowercase
            if self.include_digits.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("No Character Sets", "Please select at least one character type.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, password)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number greater than 3 for password length.")

    def copy_to_clipboard(self):
        password = self.password_output.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Nothing to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
