from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    correo: str
    rol: str