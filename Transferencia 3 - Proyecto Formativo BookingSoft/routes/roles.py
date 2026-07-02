from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.rol import Rol
from schemas.rol import RolSchema

router = APIRouter()

@router.post("/roles")
def crear_rol(datos: RolSchema, db: Session = Depends(get_db)):
    nuevo = Rol(nombre=datos.nombre, descripcion=datos.descripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Rol creado ✅", "rol": nuevo}

@router.get("/roles")
def listar_roles(db: Session = Depends(get_db)):
    return db.query(Rol).all()

@router.put("/roles/{id}")
def actualizar_rol(id: int, datos: RolSchema, db: Session = Depends(get_db)):
    rol = db.query(Rol).filter(Rol.id == id).first()
    rol.nombre = datos.nombre
    rol.descripcion = datos.descripcion
    db.commit()
    return {"mensaje": "Rol actualizado ✅"}

@router.delete("/roles/{id}")
def eliminar_rol(id: int, db: Session = Depends(get_db)):
    rol = db.query(Rol).filter(Rol.id == id).first()
    if not rol:
        return {"error": "Rol no encontrado"}
    db.delete(rol)
    db.commit()
    return {"mensaje": "Rol eliminado ✅"}
