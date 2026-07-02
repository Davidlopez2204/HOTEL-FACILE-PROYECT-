from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Servicio(Base):
    __tablename__ = "servicio"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    tipo_servicio_id = Column(Integer)
    precio_base = Column(Float)
    activo = Column(Boolean, default=True)
