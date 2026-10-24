from src.tasks.dtos import TaskSchema

def create_task(body:TaskSchema):
    return {"status":"Task Created Sucessfully..."}