from pydantic import BaseModel

class SNewDoctors(BaseModel):
    first_name: str
    last_name: str
    specialization: str
    contact_phone: str
