"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue (Navigation Draft)
Short Desc: Setup Home Dashboard and basic navigation to Timer and Task Manager windows.
"""

import tkinter as tk
from tkinter import messagebox

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("400x400")
        self.configure(bg="white")

        self.welcomeLabel = tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white")
        self.welcomeLabel.pack(pady=20)

        tk.Button(self, text="Open Timer", command=self.openTimer).pack(pady=5)
        tk.Button(self, text="Open Task Manager", command=self.openTaskManager).pack(pady=5)
        tk.Button(self, text="Exit", command=self.exitApp).pack(pady=5)

    def openTimer(self):
        TimerWindow(self)

    def openTaskManager(self):
        TaskManagerWindow(self)

    def exitApp(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.destroy()

class TimerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pomodoro Timer")
        self.geometry("300x200")
        self.configure(bg="white")
        tk.Label(self, text="Timer Window (Coming Soon)", font=("Arial", 14)).pack(pady=20)

class TaskManagerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Task Manager")
        self.geometry("300x200")
        self.configure(bg="white")
        tk.Label(self, text="Task Manager Window (Coming Soon)", font=("Arial", 14)).pack(pady=20)

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()