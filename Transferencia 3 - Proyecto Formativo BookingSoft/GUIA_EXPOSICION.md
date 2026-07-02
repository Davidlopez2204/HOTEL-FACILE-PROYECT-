# 📋 Guía de Exposición – BookingSoft API
## Proyecto Formativo | Hotel Facile

---

## ¿Qué es este proyecto?

Es una **API REST** construida con **FastAPI** y conectada a una base de datos real **PostgreSQL** corriendo bajo **Docker Compose**. Gestiona todas las tablas del sistema hotelero BookingSoft: clientes, habitaciones, reservas, facturas, pagos, servicios y eventos.

---

## 🗂️ Estructura de carpetas

```
Transferencia 3 - Proyecto Formativo BookingSoft/
│
├── main.py              → Punto de entrada de la app
├── database.py          → Conexión a PostgreSQL (Puerto 5434)
├── requirements.txt     → Librerías necesarias (incluye email-validator)
├── docker-compose.yml   → Automatización de la base de datos en Docker
│
├── middleware/
│   └── cors.py          → Configuración del CORS
│
├── models/              → Define las tablas en la Base de Datos (SQLAlchemy)
│   ├── rol.py
│   ├── usuario.py
│   ├── cliente.py
│   ├── habitacion.py
│   ├── reserva.py
│   ├── factura.py
│   ├── pago.py
│   ├── servicio.py
│   └── evento.py
│
├── schemas/             → Validaciones de parámetros (Pydantic / Field)
│   ├── rol.py
│   ├── usuario.py
│   ├── cliente.py
│   ├── habitacion.py
│   ├── reserva.py
│   ├── factura.py
│   ├── pago.py
│   ├── servicio.py
│   └── evento.py
│
└── routes/              → Puntos de entrada (endpoints) HTTP de la API
    ├── roles.py
    ├── usuarios.py
    ├── clientes.py
    ├── habitaciones.py
    ├── reservas.py
    ├── facturas.py
    ├── pagos.py
    ├── servicios.py
    └── eventos.py
```

---

## 📁 Componentes y Validaciones Clave

### `docker-compose.yml`
Permite levantar el servicio de base de datos PostgreSQL de forma aislada y rápida en el puerto `5434`.

### `schemas/` (Validaciones con Pydantic)
Siguiendo la guía de validación del docente, implementamos restricciones robustas usando `Field` y `EmailStr`:
- **Longitud Mínima (`min_length`):** Para nombres, apellidos y contraseñas (ej. mínimo 3 caracteres en nombres y 6 en contraseñas).
- **Rangos Numéricos (`gt=0`):** En identificadores extranjeros (`rol_id`, `cliente_id`) y propiedades numéricas (`piso`, `capacidad`) para que no existan valores vacíos o ilógicos.
- **Formato de Correo Electrónico (`EmailStr`):** Valida la sintaxis correcta del correo electrónico en tiempo de ejecución.

### `routes/` (Seguridad en Endpoints)
Cada ruta (GET, POST, PUT, DELETE) incluye validación de existencia antes de procesar cambios, lo que evita errores de servidor como `NoneType` al intentar borrar o modificar registros que no existen.

---

## 🔌 Conexión a la base de datos

- **Motor:** PostgreSQL 16
- **Tecnología:** Docker Compose (`postgres_hotel`)
- **Puerto local:** 5434
- **Base de datos:** `hotel_facile`

---

## 🛣️ Rutas disponibles (Endpoints)

| Tabla       | POST | GET | PUT | DELETE |
|-------------|------|-----|-----|--------|
| /roles      | ✅   | ✅  | ✅  | ✅     |
| /usuarios   | ✅   | ✅  | ✅  | ✅     |
| /clientes   | ✅   | ✅  | ✅  | ✅     |
| /habitaciones | ✅ | ✅  | ✅  | ✅     |
| /reservas   | ✅   | ✅  | ✅  | ✅     |
| /facturas   | ✅   | ✅  | ✅  | ✅     |
| /pagos      | ✅   | ✅  | ✅  | ✅     |
| /servicios  | ✅   | ✅  | ✅  | ✅     |
| /eventos    | ✅   | ✅  | ✅  | ✅     |

---

## ▶️ Cómo correr el proyecto

```bash
# 1. Iniciar base de datos con Docker Compose
docker compose up -d

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Correr el servidor
uvicorn main:app --reload
```

Luego abre en el navegador:
```
http://127.0.0.1:8000/docs
```

---

## 💬 Posibles preguntas del profesor

**¿Por qué es importante validar en el Backend si ya se valida en el Frontend?**
> Porque un usuario malintencionado o un cliente externo puede saltarse el Frontend (usando herramientas como Postman) y enviar datos corruptos directamente a la API. Validar en el Backend garantiza la integridad final de la base de datos.

**¿Qué es la librería `email-validator`?**
> Es una dependencia integrada con Pydantic que verifica no solo que el texto contenga un "@", sino que tenga el formato de dominio correcto de un correo electrónico.

**¿Cómo maneja la API los registros inexistentes en peticiones PUT/DELETE?**
> Antes de ejecutar la acción en SQLAlchemy, hacemos una consulta rápida para comprobar si el ID existe. Si no existe, devolvemos un mensaje controlado en lugar de dejar que el sistema falle con un error de ejecución de Python.
