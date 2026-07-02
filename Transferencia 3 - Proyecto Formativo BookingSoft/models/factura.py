from sqlalchemy import Column, Integer, Float
from database import Base

class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    reserva_id = Column(Integer)
    descuento = Column(Float, default=0)
    total = Column(Float, default=0)
