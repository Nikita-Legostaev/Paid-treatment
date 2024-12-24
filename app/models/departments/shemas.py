from pydantic import BaseModel
from datetime import date

class SNewDepartments(BaseModel):
    departament_name: str
    location: str
