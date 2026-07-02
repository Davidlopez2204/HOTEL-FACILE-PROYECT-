from pydantic import BaseModel, Field
from typing import Optional

class RolSchema(BaseModel):
    nombre: str = Field(..., min_length=3, description="El nombre del rol debe tener al menos 3 caracteres")
    descripcion: Optional[str] = None
