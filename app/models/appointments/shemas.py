from pydantic import BaseModel

class SNewStaff(BaseModel):
    fullname: str
    position: str
    phone: str
