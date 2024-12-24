from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter

from app.models.appointments.repositpries import AppointmentsRepositories
from app.models.appointments.shemas import SNewAppointments


router = APIRouter(
    prefix="/appointments",
    tags=["appointments"],
)


@router.get("/all")
async def get_all_appointments(offset: int = 0, limit: int = 10):
    all_appointments = await AppointmentsRepositories.get_all()
    return all_appointments[offset:limit]

@router.post("/add_appointments")
async def add_appointments(
    SNewAppointments: SNewAppointments,
):
    added_appointments = await AppointmentsRepositories.add(
        patient_id=SNewAppointments.patient_id,
        doctor_id=SNewAppointments.doctor_id,
        departament_id=SNewAppointments.departament_id,
        service_id=SNewAppointments.service_id,
        appointment_date=SNewAppointments.appointment_date,
        payment_status=SNewAppointments.payment_status,

    )
    return {"detail": "Успешно"}


@router.delete("/remove/{appointments_id}")
async def remove_appointments(
    appointments_id: int,
):
    appointments = await AppointmentsRepositories.find_one_or_none(id=appointments_id)
    if not appointments:
        raise HTTPException(status_code=404, detail="Не найдена")
    await AppointmentsRepositories.delete(id=appointments_id)
    return {"detail": "Успешно удалёно"}


@router.patch("/edit/{appointments_id}")
async def update_appointments(
    appointments_id: int,
    SNewAppointments: SNewAppointments,  
    ):
    appointments = await AppointmentsRepositories.find_by_id(id=appointments_id)
    if not appointments:
        raise HTTPException(status_code=404, detail="Не найден")
    await AppointmentsRepositories.update(id=appointments_id, **SNewAppointments.model_dump())
    return {"detail": "Успешно изменёно"}

@router.get("/count")
async def count_stock():
    count = await AppointmentsRepositories.count()
    return {"count": count}
