from sqlalchemy import Column, Integer, String, Float
from database import Base

class Pago(Base):
    __tablename__ = "pago"

    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer)
    usuario_id = Column(Integer)
    monto = Column(Float)
    referencia_pago = Column(String(100))
    tipo_pago = Column(String(20))
    estado_pago = Column(String(20), default="pendiente")
