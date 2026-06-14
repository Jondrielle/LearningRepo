from fastapi import APIRouter 
from schemas.task import CreateTask, Task

task_router = APIRouter()

tasks = []
next_task_id = 1

@task_router.get("/", response_model=list[Task])
async def get_tasks():
	return tasks

@task_router.post("/tasks", response_model=Task)
async def add_task(task: CreateTask):
	global next_task_id

	new_task = Task(
		id = next_task_id,
		name = task.name,
		description = task.description,
		is_complete = False
	)

	tasks.append(new_task)

	next_task_id += 1
	return new_task

@task_router.delete("/tasks/{task_id}")
async def delete_task():
	return {"Message" : "Delete a task"}

