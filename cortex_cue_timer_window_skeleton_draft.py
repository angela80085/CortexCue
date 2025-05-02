"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue (Timer Window Skeleton Draft)
Short Desc: Adds a separate Pomodoro Timer window with input field and placeholder start button.
"""

import tkinter as tk

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("400x400")
        self.configure(bg="white")

        tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        tk.Button(self, text="Open Timer", command=self.openTimer).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy).pack(pady=5)

    def openTimer(self):
        TimerWindow(self)

class TimerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pomodoro Timer")
        self.geometry("300x200")
        self.configure(bg="white")

        tk.Label(self, text="Enter minutes:", bg="white").pack(pady=5)
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        tk.Label(self, text="Timer: 00:00", font=("Arial", 14), bg="white").pack(pady=10)
        tk.Button(self, text="Start", command=self.placeholder).pack(pady=5)

    def placeholder(self):
        print("Start clicked")

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()