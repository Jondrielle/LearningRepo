from pydantic import BaseModel


class TaskCreate(BaseModel):
	name: str
	description: str | None = None

class Task(BaseModel):
	id: int
	name: str
	description: str | None = None
	is_complete: bool = False