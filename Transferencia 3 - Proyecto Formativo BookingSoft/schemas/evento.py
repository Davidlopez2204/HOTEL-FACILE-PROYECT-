from pydantic import BaseModel
from typing import Optional
from datetime import date

class EventoSchema(BaseModel):
    nombre: str
    cliente_id: Optional[int] = None
    estado_evento_id: Optional[int] = None
    tipo_evento: Optional[str] = None
    fecha: date
    cantidad_personas: Optional[int] = None
    precio: Optional[float] = None
    observaciones: Optional[str] = None
