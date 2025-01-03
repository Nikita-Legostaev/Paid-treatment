from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter
from datetime import date

from app.models.patients.repositpries import PatientsRepositories
from app.models.patients.shemas import SNewPatients


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


@router.get("/all")
async def get_all_patients(offset: int = 0, limit: int = 10):
    all_patients = await PatientsRepositories.get_all()
    return all_patients[offset:limit]

@router.post("/add_patients")
async def add_patients(
    SNewPatients: SNewPatients,
):
    added_patients = await PatientsRepositories.add(
        first_name=SNewPatients.first_name,
        last_name=SNewPatients.last_name,
        birth_date=SNewPatients.birth_date,
        gender=SNewPatients.gender,
        contact_phone=SNewPatients.contact_phone,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{patients_id}")
async def remove_patients(
    patients_id: int,
):
    patients = await PatientsRepositories.find_one_or_none(id=patients_id)
    if not patients:
        raise HTTPException(status_code=404, detail="Не найдена")
    await PatientsRepositories.delete(id=patients_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{patients_id}")
async def update_patients(
    patients_id: int,
    SNewPatients: SNewPatients,  
    ):
    patients = await PatientsRepositories.find_by_id(id=patients_id)
    if not patients:
        raise HTTPException(status_code=404, detail="Не найден")
    await PatientsRepositories.update(id=patients_id, **SNewPatients.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/search/")
async def search_products(
    first_name: str | None = None,
    last_name: str | None = None,
    birth_date: date | None = None,
    gender: str | None = None,
    contact_phone: str | None = None,
    offset: int = 0, limit: int = 10,
    ):
    filter_params = {key: value for key, value in locals().items() if value is not None and key not in ['offset', 'limit']}
    
    products = await PatientsRepositories.get_all(**filter_params)
    
    if not products:
        raise HTTPException(status_code=404, detail="Пациент не найден")
    
    return products[offset:offset + limit]

@router.get("/count")
async def count_stock():
    count = await PatientsRepositories.count()
    return {"count": count}
