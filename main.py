from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

tasks = []

@app.get("/tasks/")
def read_tasks():
    return tasks

@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def read_task(task_id:int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task Nahi Mila")

@app.put("/tasks/{task_id}")
def update_task(task_id:int, task_update: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task Nahi Mila")

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404, detail="Task Nahi Mila")

@app.get("/")
def home():
    return {"home":"you are in home"}