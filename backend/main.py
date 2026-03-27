from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

origins = ["*"]  # TEMP (to fix your CORS quickly)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Atlas connection
client = MongoClient(
    "mongodb+srv://ruchitamoger:Ruchita%40123@cluster0.d24do.mongodb.net/taskdb?retryWrites=true&w=majority"
)

db = client["taskdb"]
tasks_collection = db["tasks"]