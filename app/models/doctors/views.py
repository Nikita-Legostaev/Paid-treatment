from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.doctors.repositpries import DoctorsRepositories
from app.models.doctors.shemas import SNewDoctors


router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
)


@router.get("/all")
async def get_all_doctors(offset: int = 0, limit: int = 10):
    all_doctors = await DoctorsRepositories.get_all()
    return all_doctors[offset:limit]

@router.post("/add_doctors")
async def add_doctors(
    SNewDoctors: SNewDoctors,
):
    added_doctors = await DoctorsRepositories.add(
        first_name=SNewDoctors.first_name,
        last_name=SNewDoctors.last_name,
        specialization=SNewDoctors.specialization,
        contact_phone=SNewDoctors.contact_phone,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{doctors_id}")
async def remove_doctors(
    doctors_id: int,
):
    doctors = await DoctorsRepositories.find_one_or_none(id=doctors_id)
    if not doctors:
        raise HTTPException(status_code=404, detail="Не найдена")
    await DoctorsRepositories.delete(id=doctors_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{doctors_id}")
async def update_doctors(
    doctors_id: int,
    SNewDoctors: SNewDoctors,  
    ):
    doctors = await DoctorsRepositories.find_by_id(id=doctors_id)
    if not doctors:
        raise HTTPException(status_code=404, detail="Не найден")
    await DoctorsRepositories.update(id=doctors_id, **SNewDoctors.model_dump())
    return {"detail": "Успешно изменёно"}


@router.get("/count")
async def count_stock():
    count = await DoctorsRepositories.count()
    return {"count": count}
