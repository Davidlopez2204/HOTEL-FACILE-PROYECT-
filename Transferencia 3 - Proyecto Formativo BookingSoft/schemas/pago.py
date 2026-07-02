from pydantic import BaseModel
from typing import Optional

class PagoSchema(BaseModel):
    factura_id: int
    usuario_id: int
    monto: float
    referencia_pago: Optional[str] = None
    tipo_pago: str
    estado_pago: Optional[str] = "pendiente"
