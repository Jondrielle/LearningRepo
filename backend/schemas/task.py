from pydantic import BaseModel
from typing import Optional

class CreateTask(BaseModel):
	name: str
	description: Optional[str] = None

class Task(BaseModel):
	id: int
	name: str
	description: Optional[str] = None 
	is_complete: bool = False