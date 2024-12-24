from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.doctors.views import get_all_doctors
from app.models.patients.views import get_all_patients
from app.models.services.views import get_all_services
from app.models.appointments.views import get_all_appointments
from app.models.departments.views import get_all_departments
from app.models.services.repositpries import ServicesRepositories
from app.models.patients.repositpries import PatientsRepositories
from app.models.appointments.repositpries import AppointmentsRepositories
from app.models.doctors.repositpries import DoctorsRepositories

from app.models.departments.repositpries import RepositoryDepartments


router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/doctors')
async def get_doctors_html(request: Request, doctors=Depends(get_all_doctors)):
    return templates.TemplateResponse(name='doctors.html', context={'request': request, 'doctors': doctors})

@router.get('/patients')
async def get_patients_html(request: Request, patients=Depends(get_all_patients)):
    return templates.TemplateResponse(name='patients.html', context={'request': request, 'patients': patients})

@router.get('/services')
async def get_services_html(request: Request, services=Depends(get_all_services)):
    return templates.TemplateResponse(name='services.html', context={'request': request, 'services': services})

@router.get('/appointments')
async def get_appointments_html(request: Request, appointments=Depends(get_all_appointments)):
    return templates.TemplateResponse(name='appointments.html', context={'request': request, 'appointments': appointments})

@router.get('/departments')
async def get_departments_html(request: Request, departments=Depends(get_all_departments)):
    return templates.TemplateResponse(name='departments.html', context={'request': request, 'departments': departments})

@router.get('/count')
async def get_counts_html(
    request: Request,
    count_patients=Depends(PatientsRepositories.count),  # Подсчет пациентов
    count_doctors=Depends(DoctorsRepositories.count),    # Подсчет докторов
    count_departments=Depends(RepositoryDepartments.count),  # Подсчет отделов
    count_appointments=Depends(AppointmentsRepositories.count),  # Подсчет записей
    count_services=Depends(ServicesRepositories.count) 
):
    # Подготовка данных для шаблона
    counts_data = {
        'Patients': count_patients,
        'Doctors': count_doctors,
        'Departments': count_departments,
        'Appointments': count_appointments,
        'Services': count_services,
    }

    return templates.TemplateResponse(
        'counts.html', 
        context={
            'request': request, 
            'counts_data': counts_data,
            'counts_keys': list(counts_data.keys()),  # Преобразуем dict_keys в список
            'counts_values': list(counts_data.values())  # Преобразуем значения в список
        }
    )
