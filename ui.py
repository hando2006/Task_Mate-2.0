import tkinter as tk
from tkinter import messagebox
from db import get_tasks, add_task, mark_done
from voice import listen_for_task

class TaskMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskMate - Smart To-Do List")
        self.root.geometry("400x500")

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.voice_button = tk.Button(root, text="🎙️ Voice Add", command=self.voice_task)
        self.voice_button.pack(pady=5)

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(pady=10)

        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        tasks = get_tasks()
        for task in tasks:
            task_id, text, done = task
            checkbox = tk.Checkbutton(
                self.tasks_frame,
                text=f"[✔] {text}" if done else text,
                command=lambda task_id=task_id: self.mark_done(task_id),
                anchor="w",
                justify="left"
            )
            checkbox.pack(fill='x')

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            add_task(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def voice_task(self):
        task = listen_for_task()
        if task:
            add_task(task)
            self.refresh_tasks()

    def mark_done(self, task_id):
        mark_done(task_id)
        self.refresh_tasks()
