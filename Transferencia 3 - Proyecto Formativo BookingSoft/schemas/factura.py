from pydantic import BaseModel
from typing import Optional

class FacturaSchema(BaseModel):
    cliente_id: int
    reserva_id: int
    descuento: Optional[float] = 0
    total: float
