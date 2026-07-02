from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.factura import Factura
from schemas.factura import FacturaSchema

router = APIRouter()

@router.post("/facturas")
def crear_factura(datos: FacturaSchema, db: Session = Depends(get_db)):
    nuevo = Factura(cliente_id=datos.cliente_id, reserva_id=datos.reserva_id,
                    descuento=datos.descuento, total=datos.total)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Factura creada ✅", "factura": nuevo}

@router.get("/facturas")
def listar_facturas(db: Session = Depends(get_db)):
    return db.query(Factura).all()

@router.put("/facturas/{id}")
def actualizar_factura(id: int, datos: FacturaSchema, db: Session = Depends(get_db)):
    factura = db.query(Factura).filter(Factura.id == id).first()
    if not factura:
        return {"error": "Factura no encontrada"}
    factura.descuento = datos.descuento
    factura.total = datos.total
    db.commit()
    return {"mensaje": "Factura actualizada ✅"}

@router.delete("/facturas/{id}")
def eliminar_factura(id: int, db: Session = Depends(get_db)):
    factura = db.query(Factura).filter(Factura.id == id).first()
    if not factura:
        return {"error": "Factura no encontrada"}
    db.delete(factura)
    db.commit()
    return {"mensaje": "Factura eliminada ✅"}
