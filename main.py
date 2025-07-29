import tkinter as tk
from db import init_db
from ui import TaskMateApp

if __name__ == "__main__":
    init_db()  # Create the database if it doesn't exist

    root = tk.Tk()
    app = TaskMateApp(root)
    root.mainloop()
