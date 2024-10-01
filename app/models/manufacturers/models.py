from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Manufacturers(Base):
    __tablename__='manufacturers'

    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer_name: Mapped[str]
    address: Mapped[str]
    email: Mapped[str]