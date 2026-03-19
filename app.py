from flask import Flask, render_template, request, redirect
from storage import load_tasks, save_tasks

app = Flask(__name__)

@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    priority = request.form.get("priority")

    if not task:
        return redirect("/")

    tasks = load_tasks()

    tasks.append({
        "task": task,
        "done": False,
        "priority": priority
    })

    save_tasks(tasks)
    return redirect("/")


@app.route("/complete/<int:index>")
def complete_task(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)
    return redirect("/")


@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)