from fastapi import FastAPI
from app.models.doctors.views import router as doctors_router
from app.models.patients.views import router as patients_router
from app.models.services.views import router as services_router
from app.models.appointments.views import router as appointments_router
from app.models.departments.views import router as departments_router

from app.pages.router import router as router_pages

app = FastAPI()
app.include_router(doctors_router)
app.include_router(services_router)
app.include_router(patients_router)
app.include_router(router_pages)
app.include_router(appointments_router)
app.include_router(departments_router)
