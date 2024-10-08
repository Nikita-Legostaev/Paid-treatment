from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Patients(Base):
    __tablename__='patients'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[Date] = mapped_column(type_=Date)
    gender: Mapped[str]
    contact_phone: Mapped[str]