from pydantic import BaseModel

class SNewServices(BaseModel):
    service_name: str
    description: str
    price: float
