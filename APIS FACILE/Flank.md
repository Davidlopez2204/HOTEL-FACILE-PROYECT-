# API FACILE - Sistema Hotelero con FastAPI

## Importaciones

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Literal
from datetime import date
```

---

## Inicialización de la API

```python
app = FastAPI()
```

---

# MODELOS PYDANTIC

## Modelo Cliente

```python
class Cliente(BaseModel):
    id: int = Field(gt=0, description="ID mayor a 0")
    nombre: str = Field(min_length=3, max_length=80)
    cedula: str = Field(min_length=8, max_length=15)
    telefono: str = Field(min_length=10, max_length=10)
    email: EmailStr
    estado: Literal["activo", "inactivo"]
```

---

## Modelo Reserva

```python
class Reserva(BaseModel):
    id: int = Field(gt=0)
    cliente_id: int = Field(gt=0)
    cliente: str = Field(min_length=3)
    unidad: str = Field(min_length=3, max_length=10)
    fecha_entrada: date
    fecha_salida: date
    canal: Literal["directo", "booking", "airbnb"]
    estado: Literal["confirmada", "cancelada", "pendiente"]
```

---

## Modelo Login

```python
class Login(BaseModel):
    cedula: str = Field(min_length=8, max_length=15)
    password: str = Field(min_length=6, max_length=20)
```

---

## Modelo Estado de Unidad

```python
class UnidadEstado(BaseModel):
    estado: Literal[
        "disponible",
        "ocupada",
        "en mantenimiento"
    ]
```

---

# DATOS SIMULADOS

## Usuarios

```python
usuarios = [
    {
        "id": 1,
        "nombre": "Admin Facile",
        "cedula": "1001001001",
        "rol": "ADMIN",
        "sesion_activa": True
    }
]
```

---

## Clientes

```python
clientes = [
    {
        "id": 1,
        "nombre": "Carlos Mendoza",
        "cedula": "1045789321",
        "telefono": "3001234567",
        "email": "carlos@mail.com",
        "estado": "activo"
    }
]
```

---

## Unidades

```python
unidades = [
    {
        "id": 1,
        "tipo": "Habitación Sencilla",
        "numero": "101",
        "piso": 1,
        "precio_cop": 120000,
        "estado": "disponible"
    }
]
```

---

## Reservas

```python
reservas = [
    {
        "id": 1,
        "cliente_id": 1,
        "cliente": "Carlos Mendoza",
        "unidad": "101",
        "fecha_entrada": "2026-05-10",
        "fecha_salida": "2026-05-13",
        "canal": "directo",
        "estado": "confirmada"
    }
]
```

---

# RUTAS GET

## Listar Clientes

```python
@app.get("/api/v1/clientes")
def listar_clientes():
    return clientes
```

---

## Listar Reservas

```python
@app.get("/api/v1/reservas")
def listar_reservas():
    return reservas
```

---

# RUTAS POST

## Login

```python
@app.post("/api/v1/auth/login")
def login(datos: Login):

    return {
        "mensaje": "Inicio de sesión exitoso",
        "usuario": usuarios[0]
    }
```

---

## Crear Cliente

```python
@app.post("/api/v1/clientes")
def crear_cliente(cliente: Cliente):

    nuevo = cliente.dict()

    clientes.append(nuevo)

    return {
        "mensaje": "Nuevo huésped registrado en Facile",
        "cliente": nuevo
    }
```

---

## Crear Reserva

```python
@app.post("/api/v1/reservas")
def crear_reserva(reserva: Reserva):

    nueva = reserva.dict()

    reservas.append(nueva)

    return {
        "mensaje": "Nueva reserva creada correctamente",
        "reserva": nueva
    }
```

---

# RUTAS PUT

## Actualizar Cliente

```python
@app.put("/api/v1/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):

    for c in clientes:

        if c["id"] == id:

            c.update(cliente.dict())

            return {
                "mensaje": f"Cliente #{id} actualizado",
                "cliente": c
            }

    return {"error": "Cliente no encontrado"}
```

---

## Cambiar Estado de Unidad

```python
@app.put("/api/v1/unidades/{id}/estado")
def cambiar_estado_unidad(id: int, datos: UnidadEstado):

    for u in unidades:

        if u["id"] == id:

            u["estado"] = datos.estado

            return {
                "mensaje": f"Estado de unidad #{id} actualizado",
                "unidad": u
            }

    return {"error": "Unidad no encontrada"}
```

---

# RUTAS DELETE

## Desactivar Cliente

```python
@app.delete("/api/v1/clientes/{id}")
def desactivar_cliente(id: int):

    for c in clientes:

        if c["id"] == id:

            c["estado"] = "inactivo"

            return {
                "mensaje": f"Cliente #{id} desactivado",
                "cliente": c
            }

    return {"error": "Cliente no encontrado"}
```

---

# VALIDACIONES IMPLEMENTADAS

- ID mayor a 0
- Nombre mínimo 3 caracteres
- Nombre máximo 80 caracteres
- Cédula entre 8 y 15 caracteres
- Teléfono exactamente 10 caracteres
- Email válido con `EmailStr`
- Password mínimo 6 caracteres
- Password máximo 20 caracteres
- Estado restringido con `Literal`
- Canal restringido con `Literal`
- Fechas validadas con tipo `date`

---

# PRUEBAS DE ERROR 422

## Email inválido

```json
{
  "id": 1,
  "nombre": "Juan",
  "cedula": "12345678",
  "telefono": "3001234567",
  "email": "correo_mal",
  "estado": "activo"
}
```

---

## Nombre vacío

```json
{
  "id": 1,
  "nombre": "",
  "cedula": "12345678",
  "telefono": "3001234567",
  "email": "juan@mail.com",
  "estado": "activo"
}
```

---

## ID negativo

```json
{
  "id": -1,
  "nombre": "Juan",
  "cedula": "12345678",
  "telefono": "3001234567",
  "email": "juan@mail.com",
  "estado": "activo"
}
```

---

# COMMITS SUGERIDOS

```bash
feat: agregar modelos Pydantic para clientes y reservas

feat: implementar validaciones automáticas con Field

feat: validar emails y estados con EmailStr y Literal

refactor: actualizar rutas POST y PUT usando modelos

docs: agregar ejemplos de errores 422 para pruebas

feat: mejorar seguridad y control de datos en la API
```