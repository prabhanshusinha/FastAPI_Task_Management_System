from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.model import TaskModel

def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task=TaskModel(title = data["title"], description =data["description"], is_completed = data["is_completed"])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status":"Task Created Sucessfully...", "data" :new_task}


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status":"All Tasks", "data":tasks}