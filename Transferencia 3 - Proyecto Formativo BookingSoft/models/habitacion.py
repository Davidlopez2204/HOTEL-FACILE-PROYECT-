from sqlalchemy import Column, Integer, String, Text
from database import Base

class Habitacion(Base):
    __tablename__ = "habitacion"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(10), unique=True)
    piso = Column(Integer)
    capacidad = Column(Integer)
    descripcion = Column(Text)
    tipo_unidad_id = Column(Integer)
    estado_unidad_id = Column(Integer)
