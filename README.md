import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display expressions and results
entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button click
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=button_clear)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Run the application
root.mainloop()
