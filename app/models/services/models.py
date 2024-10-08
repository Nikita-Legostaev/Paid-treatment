from sqlalchemy import Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Services(Base):
    __tablename__='services'

    id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]