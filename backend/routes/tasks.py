from fastapi import APIRouter 

task_router = APIRouter()

@task_router.get("/")
async def get_tasks():
	return {"Message": "Create TODO List"}

@task_router.post("/add")
async def add_task():
	return {"Message" : "Add a task"}

@task_router.delete("/delete")
async def delete_task():
	return {"Message" : "Delete a task"}

