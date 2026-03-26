from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

origins = [
    "https://task-manager-frontend-84ne.onrender.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017")
db = client["taskdb"]
tasks_collection = db["tasks"]

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        tasks.append(task["task"])
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks_collection.insert_one({"task": task})
    return {"message": "Task added"}

@app.delete("/tasks")
def delete_task(task: str):
    tasks_collection.delete_one({"task": task})
    return {"message": "Task deleted"}