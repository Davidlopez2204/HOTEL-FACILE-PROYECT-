from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.pago import Pago
from schemas.pago import PagoSchema

router = APIRouter()

@router.post("/pagos")
def crear_pago(datos: PagoSchema, db: Session = Depends(get_db)):
    nuevo = Pago(factura_id=datos.factura_id, usuario_id=datos.usuario_id,
                 monto=datos.monto, referencia_pago=datos.referencia_pago,
                 tipo_pago=datos.tipo_pago, estado_pago=datos.estado_pago)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Pago creado", "pago": nuevo}

@router.get("/pagos")
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(Pago).all()

@router.put("/pagos/{id}")
def actualizar_pago(id: int, datos: PagoSchema, db: Session = Depends(get_db)):
    pago = db.query(Pago).filter(Pago.id == id).first()
    if not pago:
        return {"error": "Pago no encontrado"}
    pago.monto = datos.monto
    pago.estado_pago = datos.estado_pago
    pago.tipo_pago = datos.tipo_pago
    db.commit()
    return {"mensaje": "Pago actualizado"}

@router.delete("/pagos/{id}")
def eliminar_pago(id: int, db: Session = Depends(get_db)):
    pago = db.query(Pago).filter(Pago.id == id).first()
    if not pago:
        return {"error": "Pago no encontrado"}
    db.delete(pago)
    db.commit()
    return {"mensaje": "Pago eliminado"}
