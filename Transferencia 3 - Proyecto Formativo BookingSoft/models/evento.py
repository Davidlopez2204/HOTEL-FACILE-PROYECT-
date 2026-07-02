from sqlalchemy import Column, Integer, String, Float, Date, Text
from database import Base

class Evento(Base):
    __tablename__ = "evento"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150))
    cliente_id = Column(Integer)
    estado_evento_id = Column(Integer)
    tipo_evento = Column(String(100))
    fecha = Column(Date)
    cantidad_personas = Column(Integer)
    precio = Column(Float)
    observaciones = Column(Text)
