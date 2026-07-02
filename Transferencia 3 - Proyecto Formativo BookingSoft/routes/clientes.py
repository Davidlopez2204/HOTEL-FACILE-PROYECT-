from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.cliente import Cliente
from schemas.cliente import ClienteSchema

router = APIRouter()

@router.post("/clientes")
def crear_cliente(datos: ClienteSchema, db: Session = Depends(get_db)):
    nuevo = Cliente(nombre=datos.nombre, apellido=datos.apellido, identificacion=datos.identificacion,
                    telefono=datos.telefono, email=datos.email, nacionalidad=datos.nacionalidad,
                    fecha_nacimiento=datos.fecha_nacimiento, tipo_documento_id=datos.tipo_documento_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Cliente creado ✅", "cliente": nuevo}

@router.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@router.put("/clientes/{id}")
def actualizar_cliente(id: int, datos: ClienteSchema, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return {"error": "Cliente no encontrado"}
    cliente.nombre = datos.nombre
    cliente.apellido = datos.apellido
    cliente.telefono = datos.telefono
    cliente.email = datos.email
    db.commit()
    return {"mensaje": "Cliente actualizado ✅"}

@router.delete("/clientes/{id}")
def eliminar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return {"error": "Cliente no encontrado"}
    db.delete(cliente)
    db.commit()
    return {"mensaje": "Cliente eliminado ✅"}
