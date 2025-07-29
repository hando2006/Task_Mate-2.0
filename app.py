
from flask import Flask, render_template, request, redirect, url_for
from db import init_db, get_tasks, add_task, mark_done, delete_task
from voice import listen_for_task

app = Flask(__name__)
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))

@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        add_task(task)
    return redirect(url_for("index"))

@app.route("/voice", methods=["POST"])
def voice():
    task = listen_for_task()
    if task:
        add_task(task)
    return redirect(url_for("index"))

@app.route("/done/<int:task_id>")
def done(task_id):
    mark_done(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
