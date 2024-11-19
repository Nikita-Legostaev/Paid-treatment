from pydantic import BaseModel
from datetime import date

class SNewPatients(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: str
    contact_phone: str
