from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.servicio import Servicio
from schemas.servicio import ServicioSchema

router = APIRouter()

@router.post("/servicios")
def crear_servicio(datos: ServicioSchema, db: Session = Depends(get_db)):
    nuevo = Servicio(nombre=datos.nombre, tipo_servicio_id=datos.tipo_servicio_id,
                     precio_base=datos.precio_base, activo=datos.activo)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Servicio creado ✅", "servicio": nuevo}

@router.get("/servicios")
def listar_servicios(db: Session = Depends(get_db)):
    return db.query(Servicio).all()

@router.put("/servicios/{id}")
def actualizar_servicio(id: int, datos: ServicioSchema, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == id).first()
    if not servicio:
        return {"error": "Servicio no encontrado"}
    servicio.nombre = datos.nombre
    servicio.precio_base = datos.precio_base
    servicio.activo = datos.activo
    db.commit()
    return {"mensaje": "Servicio actualizado ✅"}

@router.delete("/servicios/{id}")
def eliminar_servicio(id: int, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == id).first()
    if not servicio:
        return {"error": "Servicio no encontrado"}
    db.delete(servicio)
    db.commit()
    return {"mensaje": "Servicio eliminado ✅"}
