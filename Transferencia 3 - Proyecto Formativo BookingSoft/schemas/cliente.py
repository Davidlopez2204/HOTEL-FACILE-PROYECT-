from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class ClienteSchema(BaseModel):
    nombre: str = Field(..., min_length=3, description="El nombre debe tener al menos 3 caracteres")
    apellido: str = Field(..., min_length=3, description="El apellido debe tener al menos 3 caracteres")
    identificacion: str = Field(..., min_length=5, description="La identificación debe tener al menos 5 caracteres")
    email: EmailStr = Field(..., description="Debe ser un correo electrónico válido")
    telefono: Optional[str] = Field(None, min_length=7, description="El teléfono debe tener al menos 7 caracteres")
    tipo_documento_id: Optional[int] = Field(None, gt=0, description="El tipo de documento debe ser mayor a 0")
    
    nacionalidad: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
