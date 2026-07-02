from sqlalchemy import Column, Integer, String, Date, Text
from database import Base

class Reserva(Base):
    __tablename__ = "reserva"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    habitacion_id = Column(Integer)
    tarifa_id = Column(Integer)
    estado_reserva_id = Column(Integer)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    cantidad = Column(Integer)
    observaciones = Column(Text)
    estado = Column(String(20), default="ACTIVO")
