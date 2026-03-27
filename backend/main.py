import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# CORS (allow frontend)
origins = ["*"]  # later restrict to frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Atlas connection
client = MongoClient(os.getenv("MONGO_URL"))

db = client["taskdb"]
tasks_collection = db["tasks"]


# ✅ Root route (VERY IMPORTANT)
@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


# ✅ Get tasks
@app.get("/tasks")
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        tasks.append(task.get("task"))
    return {"tasks": tasks}


# ✅ Add task
@app.post("/tasks")
def add_task(task: str):
    tasks_collection.insert_one({"task": task})
    return {"message": "Task added"}


# ✅ Delete task
@app.delete("/tasks")
def delete_task(task: str):
    tasks_collection.delete_one({"task": task})
    return {"message": "Task deleted"}