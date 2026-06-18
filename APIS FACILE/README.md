# FACILE PMS API — FastAPI
O
```python
from fastapi import FastAPI

app = FastAPI()

# =========================================
# LISTAS DE DATOS SIMULADOS
# =========================================

usuarios = [
    {"id": 1, "nombre": "Admin Facile", "cedula": "1001001001", "rol": "ADMIN", "sesion_activa": True},
    {"id": 2, "nombre": "Laura Gómez", "cedula": "1045123456", "rol": "RECEPCION", "sesion_activa": True},
    {"id": 3, "nombre": "Pedro Martínez", "cedula": "1098765432", "rol": "HOUSEKEEPING", "sesion_activa": False}
]

clientes = [
    {"id": 1, "nombre": "Carlos Mendoza", "cedula": "1045789321", "telefono": "3001234567", "email": "carlos@mail.com", "estado": "activo"},
    {"id": 2, "nombre": "María Fernanda López", "cedula": "1098234561", "telefono": "3109876543", "email": "maria@mail.com", "estado": "activo"},
    {"id": 3, "nombre": "Andrés Herrera", "cedula": "1037654892", "telefono": "3205551234", "email": "andres@mail.com", "estado": "activo"}
]

unidades = [
    {"id": 1, "tipo": "Habitación Sencilla", "numero": "101", "piso": 1, "precio_cop": 120000, "estado": "disponible"},
    {"id": 2, "tipo": "Habitación Doble", "numero": "205", "piso": 2, "precio_cop": 200000, "estado": "ocupada"},
    {"id": 3, "tipo": "Suite Familiar", "numero": "301", "piso": 3, "precio_cop": 350000, "estado": "disponible"},
    {"id": 4, "tipo": "Duplex Premium", "numero": "401", "piso": 4, "precio_cop": 500000, "estado": "en mantenimiento"}
]

reservas = [
    {"id": 1, "cliente_id": 1, "cliente": "Carlos Mendoza", "unidad": "101", "fecha_entrada": "2026-05-10", "fecha_salida": "2026-05-13", "canal": "directo", "estado": "confirmada"},
    {"id": 2, "cliente_id": 2, "cliente": "María Fernanda López", "unidad": "205", "fecha_entrada": "2026-05-11", "fecha_salida": "2026-05-14", "canal": "booking", "estado": "confirmada"}
]

estadias = [
    {"id": 1, "reserva_id": 1, "cliente": "Carlos Mendoza", "unidad": "101", "checkin": "2026-05-10 14:00", "checkout": None, "estado": "activa"},
    {"id": 2, "reserva_id": 2, "cliente": "María Fernanda López", "unidad": "205", "checkin": "2026-05-11 15:30", "checkout": None, "estado": "activa"}
]

tareas_limpieza = [
    {"id": 1, "unidad": "101", "asignada_a": "Pedro Martínez", "tipo": "limpieza salida", "estado": "pendiente"},
    {"id": 2, "unidad": "301", "asignada_a": "Pedro Martínez", "tipo": "limpieza rutinaria", "estado": "completada"}
]

facturas = [
    {"id": 1, "reserva_id": 1, "cliente": "Carlos Mendoza", "total_cop": 360000, "estado": "pendiente"},
    {"id": 2, "reserva_id": 2, "cliente": "María Fernanda López", "total_cop": 600000, "estado": "pagada"}
]

pagos = [
    {"id": 1, "factura_id": 2, "monto_cop": 600000, "metodo": "tarjeta", "tipo": "total", "estado": "aprobado"}
]

insumos = [
    {"id": 1, "nombre": "Jabón líquido", "stock_actual": 15, "stock_minimo": 20, "unidad": "litros"},
    {"id": 2, "nombre": "Toallas de baño", "stock_actual": 45, "stock_minimo": 30, "unidad": "unidades"},
    {"id": 3, "nombre": "Sábanas dobles", "stock_actual": 8, "stock_minimo": 15, "unidad": "juegos"}
]

fallas = [
    {"id": 1, "unidad": "401", "descripcion": "Aire acondicionado no enfría", "prioridad": "alta", "estado": "abierta"}
]

consumos = [
    {"id": 1, "estadia_id": 1, "servicio": "Minibar", "descripcion": "2 aguas, 1 cerveza", "monto_cop": 25000},
    {"id": 2, "estadia_id": 1, "servicio": "Lavandería", "descripcion": "3 prendas", "monto_cop": 18000}
]

auditoria = [
    {"id": 1, "usuario": "Laura Gómez", "accion": "CHECK-IN", "detalle": "Reserva #1 - Carlos Mendoza", "fecha": "2026-05-10 14:00"},
    {"id": 2, "usuario": "Admin Facile", "accion": "CREAR_UNIDAD", "detalle": "Duplex 401 agregado", "fecha": "2026-05-09 10:30"}
]

configuracion = [
    {"clave": "hora_checkin", "valor": "14:00"},
    {"clave": "hora_checkout", "valor": "12:00"},
    {"clave": "iva_porcentaje", "valor": "19"}
]

# =========================================
# RUTAS GET
# =========================================

@app.get("/api/v1/auth/me")
def datos_usuario_autenticado():
    return {"mensaje": "Datos del usuario autenticado", "usuario": usuarios[1]}

@app.get("/api/v1/clientes")
def listar_clientes():
    activos = [c for c in clientes if c["estado"] == "activo"]
    return activos

@app.get("/api/v1/unidades")
def listar_unidades():
    return unidades

@app.get("/api/v1/reservas")
def listar_reservas():
    return reservas

@app.get("/api/v1/dashboard")
def dashboard():
    return {
        "estadias_activas": len([e for e in estadias if e["estado"] == "activa"]),
        "reservas_hoy": len(reservas),
        "unidades_disponibles": len([u for u in unidades if u["estado"] == "disponible"]),
        "tareas_pendientes": len([t for t in tareas_limpieza if t["estado"] == "pendiente"]),
        "ingresos_hoy_cop": sum(p["monto_cop"] for p in pagos)
    }

# =========================================
# RUTAS POST
# =========================================

@app.post("/api/v1/auth/login")
def login():
    return {
        "mensaje": "Inicio de sesión exitoso",
        "token": "jwt_token_facile_2026",
        "usuario": usuarios[1]
    }

@app.post("/api/v1/clientes")
def crear_cliente():
    nuevo = {
        "id": 4,
        "nombre": "Valentina Ríos",
        "cedula": "1055987654",
        "telefono": "3178889900",
        "email": "valentina@mail.com",
        "estado": "activo"
    }

    clientes.append(nuevo)

    return {
        "mensaje": "Nuevo huésped registrado en Facile",
        "lista": clientes
    }

@app.post("/api/v1/reservas")
def crear_reserva():
    nueva = {
        "id": 3,
        "cliente_id": 3,
        "cliente": "Andrés Herrera",
        "unidad": "301",
        "fecha_entrada": "2026-05-15",
        "fecha_salida": "2026-05-18",
        "canal": "directo",
        "estado": "confirmada"
    }

    reservas.append(nueva)

    return {
        "mensaje": "Nueva reserva creada en Facile",
        "lista": reservas
    }

# =========================================
# RUTAS PUT
# =========================================

@app.put("/api/v1/clientes/{id}")
def actualizar_cliente(id: int):

    for c in clientes:

        if c["id"] == id:
            c["telefono"] = "3151112233"
            c["email"] = "actualizado@mail.com"

            return {
                "mensaje": f"Datos del cliente #{id} actualizados",
                "cliente": c
            }

    return {"error": "Cliente no encontrado"}

@app.put("/api/v1/unidades/{id}/estado")
def cambiar_estado_unidad(id: int):

    for u in unidades:

        if u["id"] == id:
            u["estado"] = "en mantenimiento"

            return {
                "mensaje": f"Estado de unidad #{id} actualizado",
                "unidad": u
            }

    return {"error": "Unidad no encontrada"}

# =========================================
# RUTAS DELETE
# =========================================

@app.delete("/api/v1/clientes/{id}")
def desactivar_cliente(id: int):

    for c in clientes:

        if c["id"] == id:
            c["estado"] = "inactivo"

            return {
                "mensaje": f"Cliente #{id} desactivado del sistema Facile",
                "cliente": c
            }

    return {"error": "Cliente no encontrado"}
```
