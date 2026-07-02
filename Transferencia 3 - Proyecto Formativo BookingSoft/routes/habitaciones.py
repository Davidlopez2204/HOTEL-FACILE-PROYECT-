from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.habitacion import Habitacion
from schemas.habitacion import HabitacionSchema

router = APIRouter()

@router.post("/habitaciones")
def crear_habitacion(datos: HabitacionSchema, db: Session = Depends(get_db)):
    nuevo = Habitacion(numero=datos.numero, piso=datos.piso, capacidad=datos.capacidad,
                       descripcion=datos.descripcion, tipo_unidad_id=datos.tipo_unidad_id,
                       estado_unidad_id=datos.estado_unidad_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Habitacion creada ✅", "habitacion": nuevo}

@router.get("/habitaciones")
def listar_habitaciones(db: Session = Depends(get_db)):
    return db.query(Habitacion).all()

@router.put("/habitaciones/{id}")
def actualizar_habitacion(id: int, datos: HabitacionSchema, db: Session = Depends(get_db)):
    habitacion = db.query(Habitacion).filter(Habitacion.id == id).first()
    if not habitacion:
        return {"error": "Habitacion no encontrada"}
    habitacion.piso = datos.piso
    habitacion.capacidad = datos.capacidad
    habitacion.descripcion = datos.descripcion
    habitacion.estado_unidad_id = datos.estado_unidad_id
    db.commit()
    return {"mensaje": "Habitacion actualizada ✅"}

@router.delete("/habitaciones/{id}")
def eliminar_habitacion(id: int, db: Session = Depends(get_db)):
    habitacion = db.query(Habitacion).filter(Habitacion.id == id).first()
    if not habitacion:
        return {"error": "Habitacion no encontrada"}
    db.delete(habitacion)
    db.commit()
    return {"mensaje": "Habitacion eliminada ✅"}
