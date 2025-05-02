"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue (Home GUI Layout + Placeholders Draft)
Short Desc:  Basic layout for the Cortex Cue home dashboard. Buttons link to non-functional placeholders.
"""

import tkinter as tk

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("400x500")
        self.configure(bg="white")

        tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

        # Placeholder buttons
        tk.Button(self, text="Pomodoro Timer", command=self.showComingSoon).pack(pady=5)
        tk.Button(self, text="Task Manager", command=self.showComingSoon).pack(pady=5)
        tk.Button(self, text="Mood Check-In", command=self.showComingSoon).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy).pack(pady=5)

    def showComingSoon(self):
        popup = tk.Toplevel(self)
        popup.title("Coming Soon")
        tk.Label(popup, text="Feature coming soon!", padx=20, pady=20).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()