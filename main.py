from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.model import TaskModel


Base.metadata.create_all(engine)

app=FastAPI(title="This is my Task Management Application")
