import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f5f5f5")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, font=("Arial", 14), width=25)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self.root, font=("Arial", 12), width=35, height=15, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Tasks", width=20, command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Load Tasks", width=20, command=self.load_tasks)
        self.load_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            task = self.tasks_listbox.get(selected_index)
            self.tasks.remove(task)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
