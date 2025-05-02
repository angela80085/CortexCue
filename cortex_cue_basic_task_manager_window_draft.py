"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue (Basic Task Manager Window Draft)
Short Desc: Implements a separate Task Manager window with entry field and Listbox for displaying tasks.
"""

import tkinter as tk

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("400x400")
        self.configure(bg="white")

        tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        tk.Button(self, text="Open Task Manager", command=self.openTaskManager).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy).pack(pady=5)

    def openTaskManager(self):
        TaskManagerWindow(self)

class TaskManagerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Task Manager")
        self.geometry("300x300")
        self.configure(bg="white")

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(pady=10, expand=True, fill="both")

        tk.Button(self, text="Add Task", command=self.addTask).pack(pady=5)

    def addTask(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()