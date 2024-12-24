from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.departments.repositpries import RepositoryDepartments
from app.models.departments.shemas import SNewDepartments


router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)


@router.get("/all")
async def get_all_departments(offset: int = 0, limit: int = 10):
    all_departments = await RepositoryDepartments.get_all()
    return all_departments[offset:limit]

@router.post("/add_departments")
async def add_departments(
    SNewDepartments: SNewDepartments,
):
    added_departments = await RepositoryDepartments.add(
        departament_name=SNewDepartments.departament_name,
        location=SNewDepartments.location,

    )
    return {"detail": "Успешно"}


@router.delete("/remove/{departments_id}")
async def remove_departments(
    departments_id: int,
):
    departments = await RepositoryDepartments.find_one_or_none(id=departments_id)
    if not departments:
        raise HTTPException(status_code=404, detail="Не найдена")
    await RepositoryDepartments.delete(id=departments_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{departments_id}")
async def update_departments(
    departments_id: int,
    SNewDepartments: SNewDepartments,  
    ):
    departments = await RepositoryDepartments.find_by_id(id=departments_id)
    if not departments:
        raise HTTPException(status_code=404, detail="Не найден")
    await RepositoryDepartments.update(id=departments_id, **SNewDepartments.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/count")
async def count_stock():
    count = await RepositoryDepartments.count()
    return {"count": count}
