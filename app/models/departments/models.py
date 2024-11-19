from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Departments(Base):
    __tablename__='departments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    departament_name: Mapped[str]
    location: Mapped[str]