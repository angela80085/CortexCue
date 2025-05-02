"""
Author: Angela Jones
Date written: 04/26/2025
Assignment: Final Project - Cortex Cue
Short Desc: Cortex Cue is a productivity and self-regulation tool designed for ADHD users. 
It offers a Home Dashboard, Pomodoro Timer, Task Manager, and Mood Check-In.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from tkinter import PhotoImage
from datetime import datetime
import os

class CortexCueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cortex Cue - Home Dashboard")
        self.geometry("500x600")
        self.configure(bg="white")

        # Motivational image
        self.quote_image = PhotoImage(file="motivational.png").subsample(2, 2)
        self.quote_label = tk.Label(self, image=self.quote_image, text="Success is not final, failure is not fatal: it is the courage to continue that counts.", compound="top", bg="white")
        self.quote_label.pack(pady=10)

        # Welcome label
        self.welcomeLabel = tk.Label(self, text="Welcome to Cortex Cue!", font=("Arial", 18, "bold"), bg="white")
        self.welcomeLabel.pack(pady=10)

        # Navigation buttons
        tk.Button(self, text="Open Timer", command=self.openTimer).pack(pady=5)
        tk.Button(self, text="Open Task Manager", command=self.openTaskManager).pack(pady=5)
        tk.Button(self, text="Open Mood Check-In", command=self.openMoodCheckIn).pack(pady=5)
        tk.Button(self, text="Exit", command=self.exitApp).pack(pady=5)

    def openTimer(self):
        TimerWindow(self)

    def openTaskManager(self):
        TaskManagerWindow(self)

    def openMoodCheckIn(self):
        MoodManagerWindow(self)

    def exitApp(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.destroy()

class TimerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pomodoro Timer")
        self.geometry("300x300")
        self.configure(bg="white")

        self.timeInput = tk.Entry(self)
        self.timeInput.pack(pady=10)

        self.timerLabel = tk.Label(self, text="Timer: 00:00", font=("Arial", 14), bg="white")
        self.timerLabel.pack(pady=10)

        tk.Button(self, text="Start Timer", command=self.startTimer).pack(pady=5)
        tk.Button(self, text="Pause Timer", command=self.pauseTimer).pack(pady=5)
        tk.Button(self, text="Reset Timer", command=self.resetTimer).pack(pady=5)

        self.running = False
        self.remaining = 0

    def startTimer(self):
        try:
            if not self.running:
                minutes = int(self.timeInput.get())
                self.remaining = minutes * 60
                self.running = True
                self.countdown()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def countdown(self):
        if self.running and self.remaining > 0:
            mins, secs = divmod(self.remaining, 60)
            self.timerLabel.config(text=f"Timer: {mins:02}:{secs:02}")
            self.remaining -= 1
            self.after(1000, self.countdown)
        elif self.remaining == 0:
            self.timerLabel.config(text="Time's up!")
            messagebox.showinfo("Done", "Session completed!")
            MotivationalPopup(self)

    def pauseTimer(self):
        self.running = False

    def resetTimer(self):
        self.running = False
        self.remaining = 0
        self.timeInput.delete(0, tk.END)
        self.timerLabel.config(text="Timer: 00:00")

class TaskManagerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Task Manager")
        self.geometry("500x500")
        self.configure(bg="white")

        self.taskInput = tk.Entry(self)
        self.taskInput.pack(pady=5)

        self.priorityInput = tk.Entry(self)
        self.priorityInput.pack(pady=5)
        self.priorityInput.insert(0, "Enter priority 1-5")

        tk.Button(self, text="Add Task", command=self.addTask).pack(pady=5)
        tk.Button(self, text="Delete Selected Task", command=self.deleteTask).pack(pady=5)
        tk.Button(self, text="Mark as Completed", command=self.completeTask).pack(pady=5)
        tk.Button(self, text="Save Tasks", command=self.saveTasks).pack(pady=5)

        self.taskList = tk.Listbox(self, selectmode=tk.SINGLE)
        self.taskList.pack(pady=10, expand=True, fill="both")

        self.tasks = []
        self.loadTasks()

    def addTask(self):
        task = self.taskInput.get().strip()
        priority = self.priorityInput.get().strip()
        if task and priority.isdigit():
            task_entry = f"[{priority}] {task}"
            self.tasks.insert(0, task_entry)
            self.refreshList()
            self.taskInput.delete(0, tk.END)
            self.priorityInput.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Enter a task and a valid priority (number).")

    def deleteTask(self):
        selected = self.taskList.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.refreshList()

    def completeTask(self):
        selected = self.taskList.curselection()
        if selected:
            index = selected[0]
            completed = self.tasks.pop(index)
            completed = "\u0336".join(completed) + "\u0336"  # Strikethrough
            self.tasks.append(completed)
            self.refreshList()
            self.taskList.itemconfig(tk.END, {'bg':'black', 'fg':'white'})
            MotivationalPopup(self)

    def saveTasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def loadTasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.refreshList()

    def refreshList(self):
        self.taskList.delete(0, tk.END)
        for task in self.tasks:
            self.taskList.insert(tk.END, task)

class MoodManagerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Mood Manager")
        self.geometry("500x500")
        self.configure(bg="white")

        self.dateInput = tk.Entry(self)
        self.dateInput.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.dateInput.pack(pady=5)

        self.moodInput = tk.Entry(self)
        self.moodInput.pack(pady=5)
        self.moodInput.insert(0, "Enter your mood")

        tk.Button(self, text="Add Mood", command=self.addMood).pack(pady=5)
        tk.Button(self, text="Delete Selected Mood", command=self.deleteMood).pack(pady=5)
        tk.Button(self, text="Save Moods", command=self.saveMoods).pack(pady=5)

        self.moodList = tk.Listbox(self, selectmode=tk.SINGLE)
        self.moodList.pack(pady=10, expand=True, fill="both")

        self.moods = []
        self.loadMoods()

    def addMood(self):
        date = self.dateInput.get().strip()
        mood = self.moodInput.get().strip()
        if date and mood:
            mood_entry = f"{date} - {mood}"
            self.moods.insert(0, mood_entry)
            self.moods.sort(reverse=True)
            self.refreshMoodList()
            self.dateInput.delete(0, tk.END)
            self.moodInput.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Enter a date and a mood.")

    def deleteMood(self):
        selected = self.moodList.curselection()
        if selected:
            index = selected[0]
            del self.moods[index]
            self.refreshMoodList()

    def saveMoods(self):
        with open("moods.txt", "w") as f:
            for mood in self.moods:
                f.write(mood + "\n")
        messagebox.showinfo("Saved", "Moods saved successfully!")

    def loadMoods(self):
        if os.path.exists("moods.txt"):
            with open("moods.txt", "r") as f:
                self.moods = [line.strip() for line in f.readlines()]
            self.moods.sort(reverse=True)
            self.refreshMoodList()

    def refreshMoodList(self):
        self.moodList.delete(0, tk.END)
        for mood in self.moods:
            self.moodList.insert(tk.END, mood)

class MotivationalPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("You Did It!")
        self.geometry("300x300")
        self.configure(bg="white")
        img = PhotoImage(file="motivational2.png").subsample(2,2)
        label = tk.Label(self, image=img, text="Keep up the great work!", compound="top", font=("Arial", 16), bg="white", wraplength=280, justify="center")
        label.image = img
        label.pack(pady=10)
        tk.Button(self, text="OK", command=self.destroy).pack(pady=10)

if __name__ == "__main__":
    app = CortexCueApp()
    app.mainloop()
