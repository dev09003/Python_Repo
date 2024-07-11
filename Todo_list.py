import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create a frame for the tasks
        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack()

        # Create a listbox to display the tasks
        self.listbox = tk.Listbox(self.frame_tasks, height=10, width=50)
        self.listbox.pack(side=tk.LEFT)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame_tasks)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the listbox to use the scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Create an entry field to enter new tasks
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        # Create a button to add tasks
        self.button_add_task = tk.Button(self.root, text="Add task", width=48, command=self.add_task)
        self.button_add_task.pack()

        # Create a button to delete tasks
        self.button_delete_task = tk.Button(self.root, text="Delete task", width=48, command=self.delete_task)
        self.button_delete_task.pack()

    def add_task(self):
        # Get the task from the entry field
        task = self.entry.get()

        # Check if the task is not empty
        if task!= "":
            # Add the task to the listbox
            self.listbox.insert(tk.END, task)
            # Clear the entry field
            self.entry.delete(0, tk.END)
        else:
            # Show a warning if the task is empty
            messagebox.showwarning("Warning!", "You must enter a task.")

    def delete_task(self):
        try:
            # Get the index of the selected task
            task_index = self.listbox.curselection()[0]
            # Delete the task
            self.listbox.delete(task_index)
        except:
            # Show a warning if no task is selected
            messagebox.showwarning("Warning!", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()