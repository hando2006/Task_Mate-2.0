import sqlite3

def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_done(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

# Delete a task by id
def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
