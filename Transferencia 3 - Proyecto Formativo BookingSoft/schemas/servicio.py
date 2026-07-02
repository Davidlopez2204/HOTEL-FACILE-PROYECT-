from pydantic import BaseModel, Field
from typing import Optional

class ServicioSchema(BaseModel):
    nombre: str = Field(..., min_length=3, description="El nombre del servicio debe tener al menos 3 caracteres")
    tipo_servicio_id: Optional[int] = None
    precio_base: Optional[float] = None
    activo: Optional[bool] = True
