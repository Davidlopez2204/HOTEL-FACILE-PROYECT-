# BookingSoft — Tareas Técnicas Sprint 1
### Sistema de Gestión Hotelera · Apartamentos Facile · El Chicó, Bogotá
**SENA · Análisis y Desarrollo de Software · Instructor: Jesús Ropero Barbosa**

---

## Descripción del Módulo

El módulo de usuarios tiene como objetivo administrar el personal registrado en BookingSoft y controlar el acceso a la plataforma mediante autenticación y roles.

En el sistema existirán los siguientes roles:

- `ADMINISTRADOR`
- `RECEPCIONISTA`
- `AMA_LLAVES`
- `MANTENIMIENTO`

Por defecto, todo usuario registrado tendrá el rol `RECEPCIONISTA`.

Los roles con acceso completo al panel serán `ADMINISTRADOR` y `RECEPCIONISTA`. Los demás roles tendrán acceso limitado a los módulos correspondientes a su función en el hotel.

---

## Requisitos Funcionales

| ID | Descripción |
|----|-------------|
| RF01 | El sistema deberá permitir registrar usuarios dentro de la plataforma |
| RF02 | El sistema deberá permitir visualizar el listado de usuarios registrados |
| RF03 | El sistema deberá permitir consultar la información detallada de un usuario |
| RF04 | El sistema deberá permitir la autenticación mediante correo y contraseña |
| RF05 | El sistema deberá permitir finalizar la sesión activa |
| RF06 | El sistema deberá permitir al administrador cambiar el rol de un usuario |
| RF07 | El sistema deberá validar correo y contraseña antes de permitir el acceso |
| RF08 | El sistema deberá almacenar las contraseñas cifradas mediante bcrypt |
| RF09 | El sistema deberá controlar el acceso según el rol asignado |
| RF10 | El sistema deberá permitir registrar usuarios activos e inactivos |

---

## Requisitos No Funcionales

| ID | Descripción |
|----|-------------|
| RNF01 | La API deberá responder en formato JSON |
| RNF02 | La base de datos utilizada será **PostgreSQL** |
| RNF03 | El backend será desarrollado con **Python y FastAPI** |
| RNF04 | El frontend será desarrollado con **React y JavaScript** |
| RNF05 | Las contraseñas deberán almacenarse cifradas con bcrypt |
| RNF06 | La documentación de la API será generada con **Swagger** (incluido en FastAPI) |
| RNF07 | La aplicación deberá ejecutarse en contenedores mediante **Docker** |
| RNF08 | La aplicación deberá utilizar variables de entorno para configuración sensible |
| RNF09 | El desarrollo se realizará en **Visual Studio Code** y **Antigravity** |

---

## Product Backlog — Sprint 1

| ID | Historia de Usuario | Prioridad | Puntos | Sprint |
|----|---------------------|-----------|--------|--------|
| HU01 | Registrar Usuario | Alta | 5 | Sprint 1 |
| HU02 | Iniciar Sesión | Alta | 13 | Sprint 1 |
| HU03 | Consultar Usuarios | Alta | 8 | Sprint 1 |
| HU04 | Consultar Usuario Específico | Media | 5 | Sprint 1 |
| HU05 | Cerrar Sesión | Media | 3 | Sprint 1 |

**Total Sprint 1: 34 Story Points**

---

## Sprint Backlog — Sprint 1

**Objetivo del Sprint:**
Construir el módulo de autenticación y administración básica de usuarios internos de Apartamentos Facile.

**Historias incluidas:**
- HU01 Registrar Usuario
- HU02 Iniciar Sesión
- HU03 Consultar Usuarios
- HU04 Consultar Usuario Específico
- HU05 Cerrar Sesión

---

## Historias de Usuario

### HU01 — Registrar Usuario

**Prioridad:** Alta · **Puntos:** 5 · **Sprint:** 1

**Historia:**
> Como administrador o recepcionista de Apartamentos Facile
> quiero registrar usuarios dentro del sistema BookingSoft
> para permitir la gestión del personal del hotel (recepcionistas, ama de llaves, mantenimiento) y de los huéspedes que se hospedan en Facile.

**Criterios de Aceptación:**
- Debe registrar tipo de documento (CC, CE, Pasaporte u otro)
- Debe registrar número de documento
- Debe registrar nombres y apellidos
- Debe registrar fecha de nacimiento
- Debe registrar sexo
- Debe registrar dirección
- Debe registrar teléfono / WhatsApp
- Debe registrar correo electrónico
- Debe registrar contraseña
- Debe validar que el documento sea único en el sistema
- Debe validar que el correo sea único en el sistema
- Debe cifrar la contraseña con bcrypt antes de almacenarla
- Debe asignar el rol RECEPCIONISTA por defecto
- Debe registrar el estado ACTIVO por defecto

---

### HU02 — Iniciar Sesión

**Prioridad:** Alta · **Puntos:** 13 · **Sprint:** 1

**Historia:**
> Como usuario autorizado del sistema BookingSoft
> quiero iniciar sesión con mi correo y contraseña
> para acceder al panel con los módulos de mi rol en Apartamentos Facile.

**Criterios de Aceptación:**
- Validar formato de correo electrónico
- Validar que la contraseña coincide con el hash almacenado
- Permitir acceso completo al panel a roles ADMINISTRADOR y RECEPCIONISTA; AMA_LLAVES tendrá acceso solo al estado de unidades; MANTENIMIENTO tendrá acceso solo a órdenes de mantenimiento
- Bloquear acceso si el usuario está INACTIVO
- Bloquear la cuenta 10 minutos tras 5 intentos fallidos consecutivos
- Retornar token JWT con el rol del usuario al autenticarse exitosamente
- Si es el primer acceso, forzar cambio de contraseña antes de ingresar

---

### HU03 — Consultar Usuarios

**Prioridad:** Alta · **Puntos:** 8 · **Sprint:** 1

**Historia:**
> Como administrador de Apartamentos Facile
> quiero visualizar el listado de todos los usuarios registrados
> para administrar el personal y sus accesos al sistema.

**Criterios de Aceptación:**
- Mostrar listado con: documento, nombre completo, correo, rol y estado
- Permitir ver el detalle completo de cada usuario
- Permitir cambiar el rol desde el listado
- Permitir filtrar por rol y buscar por nombre o documento
- Solo el Administrador puede acceder a esta vista

---

### HU04 — Consultar Usuario Específico

**Prioridad:** Media · **Puntos:** 5 · **Sprint:** 1

**Historia:**
> Como Administrador o Recepcionista de Apartamentos Facile
> quiero consultar la información detallada de un usuario específico ingresando su número de documento
> para verificar de manera rápida y precisa sus datos personales, rol asignado y estado dentro del hotel.

**Criterios de Aceptación:**
- Debe permitir buscar al usuario ingresando el número de documento de identidad en el buscador
- Si el usuario existe, debe mostrar toda su información detallada: tipo de documento, número de documento, nombres, apellidos, fecha de nacimiento, sexo, dirección, teléfono / WhatsApp, correo electrónico, rol y estado
- Si el usuario no existe, debe mostrar un mensaje claro indicando "Usuario no encontrado"
- El acceso debe estar restringido a usuarios autenticados con roles Administrador o Recepcionista

---

### HU05 — Cerrar Sesión

**Prioridad:** Media · **Puntos:** 3 · **Sprint:** 1

**Historia:**
> Como usuario autenticado en BookingSoft
> quiero cerrar sesión desde cualquier pantalla
> para proteger la información del hotel al cambiar de turno.

**Criterios de Aceptación:**
- El cierre de sesión se realiza desde el Frontend, sin endpoint en el backend
- Debe eliminar el token JWT almacenado en memoria de sesión
- Debe mostrar confirmación antes de cerrar: "¿Deseas cerrar sesión?"
- Debe redirigir al login tras confirmar
- El botón Atrás del navegador no puede volver al panel sin autenticarse de nuevo

---

## Modelo de Base de Datos

### Tabla `usuarios`

```sql
CREATE TABLE usuarios (
    id                 SERIAL PRIMARY KEY,
    tipo_documento     VARCHAR(20) NOT NULL,
    numero_documento   VARCHAR(20) UNIQUE NOT NULL,
    nombres            VARCHAR(100) NOT NULL,
    apellidos          VARCHAR(100) NOT NULL,
    fecha_nacimiento   DATE NOT NULL,
    sexo               VARCHAR(1) NOT NULL,
    direccion          VARCHAR(200),
    telefono           VARCHAR(20),
    correo             VARCHAR(100) UNIQUE NOT NULL,
    password           VARCHAR(255) NOT NULL,
    rol                VARCHAR(30) DEFAULT 'RECEPCIONISTA',
    estado             BOOLEAN DEFAULT TRUE,
    primer_acceso      BOOLEAN DEFAULT TRUE,
    bloqueado_hasta    TIMESTAMP NULL,
    fecha_registro     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla `intentos_login`

```sql
CREATE TABLE intentos_login (
    id           SERIAL PRIMARY KEY,
    id_usuario   INTEGER REFERENCES usuarios(id),
    timestamp    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    exitoso      BOOLEAN DEFAULT FALSE
);
```

**Restricciones:**
- `numero_documento` — UNIQUE: no puede haber dos empleados con el mismo documento
- `correo` — UNIQUE: no puede haber dos cuentas con el mismo correo
- `password` — almacena únicamente el hash bcrypt, nunca texto plano
- `rol` — valores permitidos: ADMINISTRADOR, RECEPCIONISTA, AMA_LLAVES, MANTENIMIENTO
- `estado` — TRUE = activo, FALSE = inactivo (no puede iniciar sesión)
- `primer_acceso` — TRUE obliga al cambio de contraseña en el primer login
- `bloqueado_hasta` — registra el tiempo de bloqueo tras 5 intentos fallidos

---

## Tareas Técnicas por Historia

---

### HU01 — Registrar Usuario

#### Base de Datos
- Crear tabla `usuarios` con todas las columnas y restricciones descritas arriba
- Configurar restricción UNIQUE sobre `numero_documento`
- Configurar restricción UNIQUE sobre `correo`
- Configurar valor por defecto `rol = 'RECEPCIONISTA'` y `estado = TRUE`

#### Backend
- Crear Schema `UsuarioCreateSchema` para validar los datos de entrada
- Crear Model `Usuario` con sus relaciones (SQLAlchemy)
- Crear Controller `crear_usuario()`
- Crear Route `POST /api/usuarios`
- Validar formato de correo electrónico
- Validar que el número de documento no exista previamente en la BD
- Validar que el correo no exista previamente en la BD
- Cifrar contraseña usando bcrypt antes de insertar en la BD
- Retornar HTTP 201 si el registro es exitoso
- Retornar HTTP 409 si el correo o documento ya existen

> **Nota:** Al usar SQLAlchemy como ORM, crear el modelo y ejecutar las migraciones antes de implementar el endpoint.

#### Frontend — Wireframe

```
+------------------------------------------+
|      Registrar Usuario — BookingSoft      |
+------------------------------------------+
  Tipo de Documento    [CC / CE / Pasaporte ]
  Número de Documento  [__________________  ]
  Nombres              [__________________  ]
  Apellidos            [__________________  ]
  Fecha de Nacimiento  [__________________  ]
  Sexo                 [M / F / Otro        ]
  Dirección            [__________________  ]
  Teléfono / WhatsApp  [__________________  ]
  Correo electrónico   [__________________  ]
  Contraseña           [******************  ]
                       [ 👁 mostrar/ocultar ]

          [ Registrar ]
+------------------------------------------+
```

**Reglas de Interfaz:**
- Todos los campos son obligatorios excepto dirección
- El campo contraseña debe ocultar el texto ingresado (icono ojo para mostrar/ocultar)
- Si el correo o el documento ya existen, mostrar mensaje de error junto al campo sin borrar el resto del formulario
- Tras registro exitoso, limpiar el formulario y mostrar mensaje de confirmación
- El botón **Registrar** permanece deshabilitado hasta que todos los campos obligatorios estén completos y válidos
- El rol y el estado no se muestran en el formulario — los asigna el sistema por defecto

---

### HU02 — Iniciar Sesión

#### Base de Datos
- Crear tabla `intentos_login` con campos: id, id_usuario (FK), timestamp, exitoso
- Agregar campo `bloqueado_hasta` (TIMESTAMP NULL) a la tabla `usuarios`
- El campo `password` nunca se devuelve en ninguna respuesta de la API

#### Backend
- Crear Schema `LoginSchema` para validar correo y contraseña
- Crear Controller `login()`
- Crear Route `POST /api/auth/login`
- Buscar el usuario por correo en la tabla usuarios
- Verificar si la cuenta está bloqueada (campo `bloqueado_hasta`)
- Verificar si la cuenta está activa (`estado = TRUE`)
- Comparar contraseña con hash bcrypt almacenado
- Si es correcto: generar token JWT con el rol y retornar HTTP 200
- Si es incorrecto: registrar en `intentos_login` y retornar HTTP 401 con mensaje genérico (sin revelar cuál campo falló)
- Al llegar a 5 intentos fallidos: actualizar `bloqueado_hasta = now() + 10 minutos`
- Verificar campo `primer_acceso`: si es TRUE, indicar en la respuesta que debe cambiar contraseña

> **Nota:** Al implementar autenticación con JWT, el token debe incluir el campo `rol` para que el frontend muestre solo los módulos correspondientes. Modificar el middleware de rutas protegidas para verificar el token y el rol en cada petición.

#### Frontend — Wireframe

```
+------------------------------------------+
|        BookingSoft — Apartamentos Facile  |
|              Iniciar Sesión               |
+------------------------------------------+
  Correo electrónico   [__________________  ]
  Contraseña           [******************  ]
                       [ 👁 mostrar/ocultar ]

          [ Ingresar ]

        ¿Olvidaste tu contraseña?
+------------------------------------------+
```

**Reglas de Interfaz:**
- Botón **Ingresar** deshabilitado si algún campo está vacío
- Mostrar mensaje de error genérico bajo el formulario si las credenciales son incorrectas
- Mostrar tiempo restante de bloqueo si la cuenta está bloqueada temporalmente
- Al autenticarse exitosamente, guardar el token JWT y redirigir al panel mostrando solo los módulos del rol del empleado
- Si `primer_acceso = TRUE`, redirigir obligatoriamente a la pantalla de cambio de contraseña antes de mostrar el panel

---

### HU03 — Consultar Usuarios

#### Base de Datos
- No requiere tablas nuevas — usa la tabla `usuarios` existente

#### Backend
- Crear Route `GET /api/usuarios` — retorna listado paginado de usuarios
- Implementar filtros por rol y búsqueda por nombre/documento como query params
- Solo accesible con rol ADMINISTRADOR (validar en middleware)

#### Frontend — Wireframe

```
+--------------------------------------------------------------+
|   Usuarios — BookingSoft                                     |
+--------------------------------------------------------------+
  Buscar: [________________] Filtrar por rol: [Todos ▼]

  Documento   Nombre         Correo             Rol          Estado    Acciones
  ----------  -------------  -----------------  -----------  --------  --------
  1234567890  Laura García   laura@facile.com   Recep.       Activo    [Ver] [Cambiar Rol]
  9876543210  Carlos Mesa    carlos@facile.com  Admin.       Activo    [Ver] [Cambiar Rol]
+--------------------------------------------------------------+
```

**Reglas de Interfaz:**
- La tabla debe ser paginada (máximo 20 registros por página)
- El estado activo se muestra en verde y el inactivo en rojo
- El botón **Cambiar Rol** abre un modal de confirmación antes de aplicar el cambio
- Si no hay usuarios, mostrar: "No hay usuarios registrados en el sistema"

---

### HU04 — Consultar Usuario Específico

#### Base de Datos
- No requiere tablas nuevas

#### Backend
- Crear Route `GET /api/usuarios/{numero_documento}` — busca por número de documento
- Retornar HTTP 404 con mensaje "Usuario no encontrado" si no existe

#### Frontend — Wireframe

```
+------------------------------------------+
|   Detalle de Usuario — BookingSoft        |
+------------------------------------------+
  Documento:         1234567890
  Nombre:            Laura García
  Correo:            laura@facile.com
  Rol:               Recepcionista
  Estado:            Activo
  Teléfono:          3001234567
  Dirección:         Calle 97 #21-62
  Fecha de registro: 2026-01-15

          [ Editar ]
+------------------------------------------+
```

**Reglas de Interfaz:**
- Los datos se muestran en modo solo lectura
- Si el usuario no existe, mostrar mensaje de error junto al campo de búsqueda
- El botón **Editar** lleva a la vista de modificación del usuario

---

### HU05 — Cerrar Sesión

#### Base de Datos
- No requiere cambios en base de datos

#### Backend
- No requiere endpoint — el cierre de sesión es completamente del lado del cliente

#### Frontend

```javascript
function logout() {
  sessionStorage.removeItem("token");
  sessionStorage.clear();
  window.location.href = "/login";
}
```

**Reglas de Interfaz:**
- El botón **Cerrar sesión** debe ser visible en la barra superior del panel en todo momento
- Mostrar modal de confirmación: "¿Deseas cerrar sesión?"
- Al confirmar, eliminar el token y redirigir al login
- Tras cerrar sesión, el botón Atrás del navegador no puede volver al panel sin autenticarse de nuevo

---

## Arquitectura del Backend — FastAPI

```
app/
├── config/
│   └── database.py           ← conexión a PostgreSQL con SQLAlchemy
│
├── models/
│   └── usuario_model.py      ← modelo de la tabla usuarios
│
├── schemas/
│   └── usuario_schema.py     ← validación de datos de entrada y salida (Pydantic)
│
├── controllers/
│   └── usuario_controller.py ← lógica del negocio
│
├── routes/
│   └── usuario_routes.py     ← endpoints REST
│
├── utils/
│   └── response.py           ← función de respuesta estándar JSON
│
├── .env                      ← variables de entorno (nunca subir a GitHub)
└── main.py                   ← punto de entrada de la API
```

**Responsabilidad de cada capa:**

| Capa | Responsabilidad |
|------|----------------|
| `config/` | Gestiona la conexión a PostgreSQL |
| `models/` | Representa las tablas de la base de datos |
| `schemas/` | Valida los datos de entrada y salida con Pydantic |
| `controllers/` | Implementa la lógica del negocio |
| `routes/` | Expone los endpoints REST |
| `utils/` | Contiene funciones reutilizables (respuesta estándar) |

---

## Arquitectura del Frontend — React

```
frontend/
├── src/
│   ├── pages/
│   │   ├── Login.jsx
│   │   ├── Usuarios.jsx
│   │   ├── UsuarioCreate.jsx
│   │   └── UsuarioDetail.jsx
│   │
│   ├── components/
│   │   └── Navbar.jsx
│   │
│   ├── services/
│   │   └── userService.js       ← consumo de la API
│   │
│   ├── controllers/
│   │   └── userController.js    ← manipulación del DOM / estado
│   │
│   ├── auth/
│   │   └── auth.js              ← control de autenticación y token JWT
│   │
│   └── utils/
│       └── api.js               ← configuración base de Axios/fetch
│
└── .env                         ← variables de entorno del frontend
```

**Patrón de responsabilidades:**
- `services/` → Consumo de la API REST
- `controllers/` → Manipulación del estado de React
- `auth/` → Control de autenticación y protección de rutas
- `utils/` → Funciones reutilizables

---

## Tabla de Endpoints del Módulo

| Módulo | Requerimiento | Método | Endpoint | Controlador | Descripción |
|--------|--------------|--------|----------|-------------|-------------|
| Usuarios | Registrar | POST | `/api/usuarios` | `crear_usuario()` | Crea un nuevo usuario |
| Usuarios | Login | POST | `/api/auth/login` | `login()` | Autentica y retorna JWT |
| Usuarios | Listar | GET | `/api/usuarios` | `listar_usuarios()` | Lista todos los usuarios |
| Usuarios | Detalle | GET | `/api/usuarios/{doc}` | `obtener_usuario()` | Retorna un usuario por documento |
| Usuarios | Cambiar rol | PUT | `/api/usuarios/{doc}/rol` | `cambiar_rol()` | Modifica el rol de un usuario |

---

## Flujo Completo (OBLIGATORIO entender)

```
React (Frontend)  →  Route (FastAPI)  →  Controller  →  PostgreSQL  →  Respuesta JSON
```

Cada endpoint sigue este patrón:
1. Recibir datos
2. Validar datos (Pydantic Schema)
3. Ejecutar lógica (Controller)
4. Consultar / insertar en PostgreSQL
5. Manejar errores
6. Responder con estructura estándar

---

## Respuesta Estándar de la API

Todos los endpoints responden con el mismo formato:

```json
{
  "status": "success | error",
  "message": "Descripción de lo que ocurrió",
  "data": {}
}
```

**Ejemplo éxito — Registrar usuario:**
```json
{
  "status": "success",
  "message": "Usuario registrado correctamente",
  "data": {
    "id": 1,
    "nombres": "Laura",
    "correo": "laura@facile.com",
    "rol": "RECEPCIONISTA"
  }
}
```

**Ejemplo error — Correo duplicado:**
```json
{
  "status": "error",
  "message": "El correo ya está registrado",
  "data": null
}
```

**Ejemplo error — Credenciales incorrectas:**
```json
{
  "status": "error",
  "message": "Correo o contraseña incorrectos",
  "data": null
}
```

---

## Variables de Entorno — archivo `.env`

```env
# Base de datos PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bookingsoft_facile
DB_USER=postgres
DB_PASSWORD=tu_password_aqui

# JWT
SECRET_KEY=clave_secreta_muy_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Servidor
PORT=8000
```

> ⚠️ **IMPORTANTE:** Nunca subir el archivo `.env` a GitHub. Agregarlo al `.gitignore`.

---

## Docker — Configuración básica

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: bookingsoft_facile
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: tu_password_aqui
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  api:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - .env

volumes:
  postgres_data:
```

---

## Dependencias del Proyecto

```bash
# Backend — Python / FastAPI
pip install fastapi          # Framework API
pip install uvicorn          # Servidor ASGI
pip install sqlalchemy       # ORM
pip install psycopg2-binary  # Conector PostgreSQL
pip install bcrypt           # Cifrado de contraseñas
pip install python-dotenv    # Variables de entorno
pip install pydantic         # Validaciones de esquemas
pip install python-jose      # Generación y verificación de tokens JWT
```

---

## Documentación Swagger

Una vez corriendo el proyecto, la documentación de la API estará disponible en:

```
Swagger UI:  http://localhost:8000/docs
ReDoc:       http://localhost:8000/redoc
```

Para correr el proyecto:
```bash
uvicorn app.main:app --reload
```

---

## Buenas Prácticas

**Código limpio:**
- Nombres claros y descriptivos
- Funciones pequeñas con una sola responsabilidad
- Evitar duplicación de lógica

**Seguridad:**
- Validar todos los datos de entrada con Pydantic
- No exponer contraseñas en ninguna respuesta
- Usar variables de entorno para datos sensibles
- Mensajes de error genéricos en el login (no revelar cuál campo falló)

**Organización:**
- Separar rutas y controladores en archivos distintos
- Agrupar por módulos (usuarios, reservas, etc.)
- Respuestas consistentes en todos los endpoints

**Errores comunes a evitar:**
- ❌ SQL directo dentro de las rutas
- ❌ Contraseñas o credenciales quemadas en el código
- ❌ Respuestas con formatos diferentes en cada endpoint
- ❌ No validar los datos de entrada
- ❌ Mezclar lógica de módulos distintos

---

## Pruebas de la API

Probar los endpoints con alguno de estos clientes REST:
- **Thunder Client** (extensión de VS Code) — recomendado
- **Postman**
- **Insomnia**

**Ejemplo de prueba — Crear usuario:**
```
POST http://localhost:8000/api/usuarios
Content-Type: application/json

{
  "tipo_documento": "CC",
  "numero_documento": "1234567890",
  "nombres": "Laura",
  "apellidos": "García",
  "fecha_nacimiento": "1995-03-15",
  "sexo": "F",
  "telefono": "3001234567",
  "correo": "laura@facile.com",
  "password": "Facile2026*"
}
```

**Ejemplo de prueba — Login:**
```
POST http://localhost:8000/api/auth/login
Content-Type: application/json

{
  "correo": "laura@facile.com",
  "password": "Facile2026*"
}
```

---

*BookingSoft · Apartamentos Facile · SENA ADSO · Instructor: Jesús Ropero Barbosa · 2026*
