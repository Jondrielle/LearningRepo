from fastapi import APIRouter,HTTPException 
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
async def delete_task(task_id: int):
	for task in tasks:
		if task.id == task_id:
			tasks.remove(task)
			return {"Message" : "Task deleted"}

	raise HTTPException(
		status_code = 404,
		detail = "Task not found"
	)

@task_router.patch("/tasks/{task_id}",response_model=Task)
async def update_task(task_id: int):
	for task in tasks:
		if task.id == task_id:
			task.is_complete = not task.is_complete
			return task

	raise HTTPException(
		status_code = 404,
		detail = "Task not found")

