from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.evento import Evento
from schemas.evento import EventoSchema

router = APIRouter()

@router.post("/eventos")
def crear_evento(datos: EventoSchema, db: Session = Depends(get_db)):
    nuevo = Evento(nombre=datos.nombre, cliente_id=datos.cliente_id,
                   estado_evento_id=datos.estado_evento_id, tipo_evento=datos.tipo_evento,
                   fecha=datos.fecha, cantidad_personas=datos.cantidad_personas,
                   precio=datos.precio, observaciones=datos.observaciones)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Evento creado ✅", "evento": nuevo}

@router.get("/eventos")
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(Evento).all()

@router.put("/eventos/{id}")
def actualizar_evento(id: int, datos: EventoSchema, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id == id).first()
    if not evento:
        return {"error": "Evento no encontrado"}
    evento.nombre = datos.nombre
    evento.fecha = datos.fecha
    evento.cantidad_personas = datos.cantidad_personas
    evento.precio = datos.precio
    evento.estado_evento_id = datos.estado_evento_id
    db.commit()
    return {"mensaje": "Evento actualizado ✅"}

@router.delete("/eventos/{id}")
def eliminar_evento(id: int, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id == id).first()
    if not evento:
        return {"error": "Evento no encontrado"}
    db.delete(evento)
    db.commit()
    return {"mensaje": "Evento eliminado ✅"}
