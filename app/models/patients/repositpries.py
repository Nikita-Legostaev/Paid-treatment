from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from app.models.patients.models import Patients
from app.repositories.base import BaseRepositories
from app.database import async_session
from sqlalchemy.exc import SQLAlchemyError


class PatientsRepositories(BaseRepositories):
    model = Patients