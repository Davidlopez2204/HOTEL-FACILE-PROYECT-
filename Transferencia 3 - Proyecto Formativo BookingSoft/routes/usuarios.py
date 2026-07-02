from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.usuario import Usuario
from schemas.usuario import UsuarioSchema

router = APIRouter()

@router.post("/usuarios")
def crear_usuario(datos: UsuarioSchema, db: Session = Depends(get_db)):
    nuevo = Usuario(nombre=datos.nombre, apellido=datos.apellido, cedula=datos.cedula,
                    email=datos.email, password=datos.password, rol_id=datos.rol_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Usuario creado ✅", "usuario": nuevo}

@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, datos: UsuarioSchema, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        return {"error": "Usuario no encontrado"}
    usuario.nombre = datos.nombre
    usuario.apellido = datos.apellido
    usuario.email = datos.email
    usuario.rol_id = datos.rol_id
    db.commit()
    return {"mensaje": "Usuario actualizado ✅"}

@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        return {"error": "Usuario no encontrado"}
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado ✅"}
