from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.doctors.models import Doctors
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class DoctorsRepositories(BaseRepositories):
    model = Doctors