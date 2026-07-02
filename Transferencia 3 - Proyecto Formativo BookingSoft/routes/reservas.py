from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.reserva import Reserva
from schemas.reserva import ReservaSchema

router = APIRouter()

@router.post("/reservas")
def crear_reserva(datos: ReservaSchema, db: Session = Depends(get_db)):
    nuevo = Reserva(cliente_id=datos.cliente_id, habitacion_id=datos.habitacion_id,
                    tarifa_id=datos.tarifa_id, estado_reserva_id=datos.estado_reserva_id,
                    fecha_inicio=datos.fecha_inicio, fecha_fin=datos.fecha_fin,
                    cantidad=datos.cantidad, observaciones=datos.observaciones)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Reserva creada", "reserva": nuevo}

@router.get("/reservas")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()

@router.put("/reservas/{id}")
def actualizar_reserva(id: int, datos: ReservaSchema, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == id).first()
    if not reserva:
        return {"error": "Reserva no encontrada"}
    reserva.fecha_inicio = datos.fecha_inicio
    reserva.fecha_fin = datos.fecha_fin
    reserva.observaciones = datos.observaciones
    reserva.estado_reserva_id = datos.estado_reserva_id
    db.commit()
    return {"mensaje": "Reserva actualizada"}

@router.delete("/reservas/{id}")
def eliminar_reserva(id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == id).first()
    if not reserva:
        return {"error": "Reserva no encontrada"}
    db.delete(reserva)
    db.commit()
    return {"mensaje": "Reserva eliminada"}
