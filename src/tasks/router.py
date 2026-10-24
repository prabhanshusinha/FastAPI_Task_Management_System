from fastapi import APIRouter
from src.tasks import contoller
from src.tasks.dtos import TaskSchema

task_routes=APIRouter(prefix="/tasks")


@task_routes.post("/create")
def create_task(body: TaskSchema):
    return contoller.create_task()