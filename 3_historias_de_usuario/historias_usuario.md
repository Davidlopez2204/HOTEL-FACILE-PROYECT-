# Historias de Usuario (Product Backlog)
## Proyecto: Sistema de Gestión Hotelera - BookingSoft para Facile

Este documento presenta la especificación formal del **Product Backlog** general del sistema y el detalle de las **Historias de Usuario (HU)** correspondientes al **Módulo de Usuarios**.

---

## 1. Product Backlog General

A continuación se presenta el listado de las 15 historias de usuario identificadas para el sistema, ordenadas por prioridad y sprint asignado:

| ID | Módulo | Historia | MoSCoW | Pts | Sprint |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HU-001** | Módulo 1 | Registro y gestión de usuarios | 🔴 MUST | 5 | Sprint 1 |
| **HU-002** | Módulo 2 | Iniciar Sesión | 🔴 MUST | 13 | Sprint 1 |
| **HU-003** | Módulo 2 | Consultar Usuarios del Sistema | 🔴 MUST | 8 | Sprint 1 |
| **HU-004** | Módulo 3 | Consultar Usuario Específico | 🔴 MUST | 5 | Sprint 1 |
| **HU-005** | Módulo 2 | Check-in y check-out | 🔴 MUST | 16 | Sprint 2 |
| **HU-006** | Módulo 4 | Tarifas por unidad | 🔴 MUST | 8 | Sprint 2 |
| **HU-007** | Módulo 5 | Servicios y consumos | 🔴 MUST | 18 | Sprint 3 |
| **HU-008** | Módulo 6 | Mantenimiento | 🔴 MUST | 8 | Sprint 3 |
| **HU-009** | Módulo 7 | Registro de unidades | 🔴 MUST | 18 | Sprint 3 |
| **HU-010** | Módulo 8 | Gestión financiera | 🔴 MUST | 21 | Sprint 4 |
| **HU-011** | Módulo 8 | Inventario y alertas | 🔴 MUST | 8 | Sprint 4 |
| **HU-012** | Módulo 9 | Notificaciones | 🟡 SHOULD | 5 | Sprint 3 |
| **HU-013** | Módulo 7 | Sala de Juntas / Coworking | 🔴 MUST | 8 | Sprint 3 |
| **HU-014** | Módulo 10 | Disponibilidad 24/7 | 🔴 MUST | 10 | Sprint 4 |
| **HU-015** | Módulo 11 | Reportes y ocupación | 🟡 SHOULD | 5 | Sprint 4 |

---

## 2. Especificación Detallada (Módulo de Usuarios)

### HU-001 — Registrar Usuario del Sistema

| ID | HU-001 | Título | Registrar Usuario del Sistema |
| :--- | :--- | :--- | :--- |
| **Prioridad** | 🔴 Alta — MUST HAVE | **Puntos de historia** | 5 puntos |
| **Sprint** | Sprint 1 | **Actor principal** | Administrador / Recepcionista |

#### Historia de Usuario
*   **Como:** administrador o recepcionista de Apartamentos Facile
*   **Quiero:** registrar usuarios dentro del sistema BookingSoft
*   **Para:** permitir la gestión del personal del hotel (recepcionistas, ama de llaves, mantenimiento, conserje) y de los huéspedes que se hospedan en Facile.

#### Criterios de Aceptación
*   [x] Debe registrar tipo de documento (CC, pasaporte, CE u otro — requerido por el RNT colombiano).
*   [x] Debe registrar número de documento.
*   [x] Debe registrar nombres y apellidos.
*   [x] Debe registrar fecha de nacimiento.
*   [x] Debe registrar sexo.
*   [x] Debe registrar dirección.
*   [x] Debe registrar teléfono / WhatsApp (canal principal de comunicación de Facile).
*   [x] Debe registrar correo electrónico.
*   [x] Debe registrar contraseña.
*   [x] Debe validar que el documento sea único en el sistema.
*   [x] Debe validar que el correo sea único en el sistema.
*   [x] Debe cifrar la contraseña antes de almacenarla (bcrypt).
*   [x] Debe asignar el rol RECEPCIONISTA por defecto al crear personal (configurable por el administrador).
*   [x] Debe registrar el estado ACTIVO por defecto.

#### Tareas Técnicas
*   **Base de Datos:**
    *   Crear tabla usuarios con campos: `id`, `tipo_documento`, `numero_documento` (UNIQUE), `nombres`, `apellidos`, `fecha_nacimiento`, `sexo`, `direccion`, `telefono`, `correo` (UNIQUE), `contrasena`, `rol` (ENUM: ADMINISTRADOR, RECEPCIONISTA, AMA_LLAVES, MANTENIMIENTO, CONSERJE), `estado` (BOOLEAN), `fecha_registro`.
    *   Configurar restricción UNIQUE sobre `numero_documento`.
    *   Configurar restricción UNIQUE sobre `correo`.
    *   Configurar valor por defecto `estado` = ACTIVO.
*   **Backend:**
    *   Crear Schema `UserCreateSchema` para validar los datos de entrada.
    *   Crear Model `User` con sus relaciones.
    *   Crear Controller `create_user()`.
    *   Crear Route POST `/api/usuarios`.
    *   Validar formato de correo electrónico.
    *   Validar que el número de documento no exista previamente.
    *   Cifrar contraseña usando bcrypt antes de guardar en la base de datos.
    *   Retornar HTTP 201 si el registro es exitoso.
    *   Retornar HTTP 409 si el correo o documento ya existen.
*   **Frontend — Campos del formulario / Wireframe:**
    *   Tipo de Documento (selector: CC / Pasaporte / CE / Otro)
    *   Número de Documento
    *   Nombres
    *   Apellidos
    *   Fecha de Nacimiento
    *   Sexo (selector)
    *   Dirección
    *   Teléfono / WhatsApp
    *   Correo electrónico
    *   Contraseña
    *   Botón: Registrar (deshabilitado hasta completar campos obligatorios)
*   **Reglas de Interfaz:**
    *   Todos los campos son obligatorios excepto dirección.
    *   El campo contraseña debe ocultar el texto ingresado (icono de ojo para mostrar/ocultar).
    *   Si el correo o el documento ya existen, mostrar mensaje de error junto al campo correspondiente sin borrar el resto del formulario.
    *   Tras un registro exitoso, limpiar el formulario y mostrar mensaje de confirmación.
    *   El rol y el estado no se muestran en el formulario — los asigna el sistema por defecto.
    *   El botón Registrar permanece deshabilitado hasta que todos los campos obligatorios estén completos.
*   **Jira:**
    *   Crear tarea 'HU-001 Registrar Usuario' con subtareas para Base de Datos, Backend y Frontend. Asignar responsable por área.

---

### HU-002 — Iniciar Sesión

| ID | HU-002 | Título | Iniciar Sesión |
| :--- | :--- | :--- | :--- |
| **Prioridad** | 🔴 Alta — MUST HAVE | **Puntos de historia** | 13 puntos |
| **Sprint** | Sprint 1 | **Actor principal** | Todo el personal de Facile |

#### Historia de Usuario
*   **Como:** usuario autorizado del sistema BookingSoft
*   **Quiero:** iniciar sesión con mi correo y contraseña
*   **Para:** acceder al panel de BookingSoft con los módulos correspondientes a mi rol en Apartamentos Facile.

#### Criterios de Aceptación
*   [x] Validar formato de correo electrónico.
*   [x] Validar que la contraseña coincida con el hash almacenado (bcrypt).
*   [x] Permitir acceso únicamente a roles: ADMINISTRADOR y RECEPCIONISTA para el panel completo.
*   [x] Roles con acceso limitado: AMA_LLAVES (solo estado de unidades), MANTENIMIENTO (solo órdenes de mantenimiento), CONSERJE (solo servicios y solicitudes).
*   [x] Bloquear acceso si el usuario está en estado INACTIVO con mensaje claro.
*   [x] Bloquear el acceso temporalmente (10 minutos) tras 5 intentos fallidos consecutivos.
*   [x] Al autenticarse, redirigir al panel mostrando solo los módulos del rol correspondiente.
*   [x] Si es el primer acceso (contraseña temporal), forzar el cambio de contraseña antes de ingresar.

#### Tareas Técnicas
*   **Base de Datos:**
    *   Tabla `intentos_login`: `id`, `id_usuario` (FK), `timestamp`, `exitoso` (BOOLEAN).
    *   Campo `bloqueado_hasta` (DATETIME, nullable) en tabla usuarios.
*   **Backend:**
    *   Crear Route POST `/api/auth/login`.
    *   Verificar correo en tabla usuarios y comparar contraseña con bcrypt.
    *   Retornar token JWT con el rol del usuario si las credenciales son correctas (HTTP 200).
    *   Retornar HTTP 401 con mensaje genérico si las credenciales son incorrectas (no revelar cuál campo falló).
    *   Retornar HTTP 403 si la cuenta está inactiva.
    *   Implementar bloqueo de 10 minutos tras 5 intentos fallidos.
    *   Registrar cada intento fallido en la tabla `intentos_login`.
*   **Frontend — Campos del formulario / Wireframe:**
    *   Campo: Correo electrónico
    *   Campo: Contraseña (con icono mostrar/ocultar)
    *   Botón: Ingresar (deshabilitado si los campos están vacíos)
    *   Enlace: ¿Olvidaste tu contraseña? (redirige a HU-005)
*   **Reglas de Interfaz:**
    *   El botón Ingresar permanece deshabilitado si algún campo está vacío.
    *   Mostrar mensaje de error genérico en caso de credenciales incorrectas.
    *   Mostrar tiempo restante de bloqueo si la cuenta está bloqueada temporalmente.
    *   Al autenticarse exitosamente, mostrar solo los módulos que corresponden al rol del usuario.
*   **Jira:**
    *   Crear tarea 'HU-002 Iniciar Sesión' con subtareas para Base de Datos, Backend y Frontend.

---

### HU-003 — Consultar Usuarios

| ID | HU-003 | Título | Consultar Usuarios del Sistema |
| :--- | :--- | :--- | :--- |
| **Prioridad** | 🔴 Alta — MUST HAVE | **Puntos de historia** | 8 puntos |
| **Sprint** | Sprint 1 | **Actor principal** | Administrador |

#### Historia de Usuario
*   **Como:** administrador de Apartamentos Facile
*   **Quiero:** visualizar el listado de todos los usuarios registrados en BookingSoft
*   **Para:** administrar el personal del hotel y sus accesos al sistema.

#### Criterios de Aceptación
*   [x] Debe mostrar el listado de usuarios con: documento, nombre completo, correo, rol y estado (activo/inactivo).
*   [x] Debe permitir ver el detalle completo de cada usuario.
*   [x] Debe permitir acceder a la opción de cambiar rol desde el listado.
*   [x] Debe permitir filtrar usuarios por rol (Administrador, Recepcionista, Ama de llaves, Mantenimiento, Conserje).
*   [x] Debe permitir buscar por nombre o número de documento.
*   [x] Solo el Administrador puede acceder a esta vista.

#### Tareas Técnicas
*   **Base de Datos:**
    *   No requiere tablas nuevas — usa la tabla usuarios existente.
*   **Backend:**
    *   Crear Route GET `/api/usuarios` — retorna listado paginado de usuarios.
    *   Crear Route GET `/api/usuarios/{id}` — retorna detalle de un usuario.
    *   Implementar filtros por rol y búsqueda por nombre/documento como query params.
    *   Solo accesible con rol ADMINISTRADOR (validar en middleware).
*   **Frontend — Campos del formulario / Wireframe:**
    *   Tabla con columnas: Documento, Nombre, Correo, Rol, Estado, Acciones
    *   Botón Ver detalle por cada fila
    *   Botón Cambiar rol por cada fila
    *   Filtros: Selector de rol + campo de búsqueda por nombre o documento
*   **Reglas de Interfaz:**
    *   La tabla debe ser paginada (máximo 20 registros por página).
    *   El botón Cambiar rol abre un modal de confirmación antes de aplicar el cambio.
    *   El estado activo se muestra en verde y el inactivo en rojo.
    *   Si no hay usuarios registrados, mostrar mensaje: "No hay usuarios en el sistema".
*   **Jira:**
    *   Crear tarea 'HU-003 Consultar Usuarios' con subtareas para Backend y Frontend.

---

### HU-004 — Consultar Usuario Específico

| ID | HU-004 | Título | Consultar Usuario Específico |
| :--- | :--- | :--- | :--- |
| **Prioridad** | 🟡 Media | **Puntos de historia** | 5 puntos |
| **Sprint** | Sprint 1 | **Actor principal** | Administrador / Recepcionista |

#### Historia de Usuario
*   **Como:** Administrador o Recepcionista de Apartamentos Facile
*   **Quiero:** Consultar la información detallada de un usuario específico ingresando su número de documento
*   **Para:** Verificar de manera rápida y precisa sus datos personales, rol asignado y estado dentro del hotel.

#### Criterios de Aceptación
*   [x] Debe permitir buscar al usuario ingresando el número de documento de identidad en el buscador.
*   [x] Si el usuario existe en el sistema, debe retornar y mostrar toda su información detallada: Tipo de documento, Número de documento, Nombres, Apellidos, Fecha de nacimiento, Sexo, Dirección, Teléfono / WhatsApp, Correo electrónico, Rol y Estado.
*   [x] Si el usuario no existe en la base de datos, el sistema debe retornar un mensaje claro indicando "Usuario no encontrado".
*   [x] El acceso a esta consulta debe estar restringido únicamente a usuarios autenticados con roles permitidos (Administrador / Recepcionista).

#### Tareas Técnicas
*   **Base de Datos:**
    *   No requiere tablas nuevas — usa la tabla usuarios existente.
*   **Backend:**
    *   Crear Route GET `/api/usuarios/documento/{numero_documento}` que retorne los datos del usuario.
    *   Implementar validación para comprobar la existencia del usuario y el formato del documento de identidad.
    *   Retornar HTTP 200 con la información detallada del usuario si existe en base de datos.
    *   Retornar HTTP 404 si el usuario no es encontrado.
*   **Frontend — Campos del formulario / Wireframe:**
    *   Campo de entrada de búsqueda (Número de Documento).
    *   Botón de buscar (o ejecución de consulta automática).
    *   Sección de visualización del perfil del usuario (tarjeta de perfil o modal con todos los campos).
*   **Reglas de Interfaz:**
    *   Mostrar indicador de carga mientras se realiza la consulta.
    *   En caso de error 404, mostrar una alerta en la UI sin desconfigurar la pantalla actual.
    *   Por motivos de seguridad, la contraseña (incluso el hash de bcrypt) jamás debe ser expuesta en el payload del JSON ni cargada en la interfaz del cliente.
*   **Jira:**
    *   Crear tarea 'HU-004 Consultar Usuario Específico' con subtareas para Backend y Frontend.
