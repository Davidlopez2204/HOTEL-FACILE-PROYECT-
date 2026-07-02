from sqlalchemy import Column, Integer, String, Text
from database import Base

class Rol(Base):
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True)
    descripcion = Column(Text)
