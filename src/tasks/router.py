from fastapi import APIRouter,Depends
from src.tasks import contoller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

task_routes=APIRouter(prefix="/tasks")


@task_routes.post("/create")
def create_task(body: TaskSchema,db= Depends(get_db)):
    return contoller.create_task(body,db)


@task_routes.get("/all_tasks")
def get_all_tasks(db= Depends(get_db)):
    return contoller.get_tasks(db)