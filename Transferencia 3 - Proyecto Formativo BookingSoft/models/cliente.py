from sqlalchemy import Column, Integer, String, Date, Text
from database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    identificacion = Column(String(100), unique=True)
    telefono = Column(String(100))
    email = Column(String(150))
    nacionalidad = Column(String(100))
    fecha_nacimiento = Column(Date)
    tipo_documento_id = Column(Integer)
