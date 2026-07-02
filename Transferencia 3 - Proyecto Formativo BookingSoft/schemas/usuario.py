from pydantic import BaseModel, Field, EmailStr

class UsuarioSchema(BaseModel):
    nombre: str = Field(..., min_length=3, description="El nombre debe tener al menos 3 caracteres")
    apellido: str = Field(..., min_length=3, description="El apellido debe tener al menos 3 caracteres")
    cedula: str = Field(..., min_length=5, description="La cédula debe tener al menos 5 caracteres")
    email: EmailStr = Field(..., description="Debe ser un correo electrónico válido")
    password: str = Field(..., min_length=6, description="La contraseña debe tener al menos 6 caracteres")
    rol_id: int = Field(..., gt=0, description="El rol_id debe ser mayor a 0")
