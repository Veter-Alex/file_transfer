from fastapi import FastAPI

app = FastAPI(
    title="File Transfer",
    description="File Transfer API",
    version="0.1.0",
)

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1"},
    {"id": 2, "title": "Task 2", "description": "Description 2"},
]


@app.get("/tasks")
async def get_tasks():
    return {"message": "Hello World"}


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    return [task for task in tasks if task.get("id") == task_id]
