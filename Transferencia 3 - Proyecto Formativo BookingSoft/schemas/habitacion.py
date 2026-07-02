from pydantic import BaseModel, Field
from typing import Optional

class HabitacionSchema(BaseModel):
    numero: str = Field(..., min_length=1, description="El número de habitación no puede estar vacío")
    piso: int = Field(..., gt=0, description="El piso debe ser mayor que 0")
    capacidad: int = Field(..., gt=0, description="La capacidad debe ser mayor que 0")
    descripcion: Optional[str] = None
    tipo_unidad_id: Optional[int] = None
    estado_unidad_id: Optional[int] = None
