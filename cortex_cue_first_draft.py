"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue (First Draft)
Short Desc: Initial setup of Cortex Cue app with basic Home Dashboard GUI.
"""

import tkinter as tk

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("400x400")
        self.configure(bg="white")

        self.welcomeLabel = tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white")
        self.welcomeLabel.pack(pady=20)

        # Only basic button for now
        tk.Button(self, text="Exit", command=self.exitApp).pack(pady=10)

    def exitApp(self):
        self.destroy()

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()