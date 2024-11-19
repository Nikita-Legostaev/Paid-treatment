from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.services.repositpries import ServicesRepositories
from app.models.services.shemas import SNewServices


router = APIRouter(
    prefix="/services",
    tags=["services"],
)


@router.get("/all")
async def get_all_services(offset: int = 0, limit: int = 10):
    all_services = await ServicesRepositories.get_all()
    return all_services[offset:limit]

@router.post("/add_services")
async def add_services(
    SNewServices: SNewServices,
):
    added_services = await ServicesRepositories.add(
        service_name=SNewServices.service_name,
        description=SNewServices.description,
        price=SNewServices.price,
    )
    return {"detail": "Успешно"}


@router.delete("/remove/{services_id}")
async def remove_services(
    services_id: int,
):
    services = await ServicesRepositories.find_one_or_none(id=services_id)
    if not services:
        raise HTTPException(status_code=404, detail="Не найдена")
    await ServicesRepositories.delete(id=services_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{services_id}")
async def update_services(
    services_id: int,
    SNewServices: SNewServices,  
    ):
    services = await ServicesRepositories.find_by_id(id=services_id)
    if not services:
        raise HTTPException(status_code=404, detail="Не найден")
    await ServicesRepositories.update(id=services_id, **SNewServices.model_dump())
    return {"detail": "Успешно изменёно"}
