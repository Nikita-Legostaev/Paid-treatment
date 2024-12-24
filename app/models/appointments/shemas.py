from pydantic import BaseModel
from datetime import date

class SNewAppointments(BaseModel):
    patient_id: int
    doctor_id: int
    departament_id: int
    service_id: int
    appointment_date: date
    payment_status: str
