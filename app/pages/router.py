from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.doctors.views import get_all_doctors
from app.models.patients.views import get_all_patients
from app.models.services.views import get_all_services


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