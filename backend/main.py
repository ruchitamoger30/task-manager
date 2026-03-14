from fastapi import FastAPI

app = FastAPI()

# Temporary task storage
tasks = []

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

@app.delete("/tasks")
def delete_task(task: str):
    if task in tasks:
        tasks.remove(task)
        return {"message": "Task removed", "tasks": tasks}
    return {"message": "Task not found"}