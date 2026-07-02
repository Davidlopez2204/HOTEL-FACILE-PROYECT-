from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReservaSchema(BaseModel):
    cliente_id: int
    habitacion_id: int
    tarifa_id: Optional[int] = None
    estado_reserva_id: Optional[int] = None
    fecha_inicio: date
    fecha_fin: date
    cantidad: Optional[int] = None
    observaciones: Optional[str] = None
