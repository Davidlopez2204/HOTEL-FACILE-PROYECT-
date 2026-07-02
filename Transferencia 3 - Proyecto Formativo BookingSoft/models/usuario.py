from sqlalchemy import Column, Integer, String, Boolean, Text
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    cedula = Column(String(20), unique=True)
    email = Column(String(150), unique=True)
    password = Column(String(255))
    activo = Column(Boolean, default=True)
    rol_id = Column(Integer)
