from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Appointments(Base):
    __tablename__='appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey('patients.id'))
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctors.id'))
    departament_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    appointment_date: Mapped[Date] = mapped_column(type_=Date)
    payment_status: Mapped[str]