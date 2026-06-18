# Contexto del Proyecto: BookingSoft (FACILE PMS)
## Sistema de Gestión de Apartahoteles — Proyecto Académico ADSO

Este documento explica de manera detallada el trasfondo operativo y técnico del proyecto **BookingSoft**, un sistema PMS (Property Management System) adaptado para Apartamentos Facile. El proyecto se estructura bajo tres preguntas clave que definen su desarrollo: **¿Por qué?**, **¿Cómo?** y **¿Para qué?**.

---

## 1. ¿Por qué? (La Problemática y Justificación)

### El Reto Operativo
Los apartahoteles modernos (como Apartamentos Facile, ubicados en El Chicó, Bogotá) operan las 24 horas del día, los 7 días de la semana. Requieren coordinar en tiempo real múltiples flujos operativos:
*   Registro y administración de usuarios (personal de recepción, limpieza, mantenimiento, conserjes y huéspedes).
*   Control de reservas y bloqueo inmediato de unidades para evitar la sobreventa.
*   Consulta de disponibilidad de habitaciones en tiempo real.
*   Reserva de espacios comunes por horas (sala de juntas / coworking) tanto para huéspedes como para clientes externos.

### Justificación de la Arquitectura Seleccionada
Para resolver esta problemática operativa de manera eficiente, robusta y ágil, se definió una arquitectura de **Monolito de Tres Capas** utilizando **FastAPI (Python)** y **React (JavaScript)**:
*   **Gestión Eficiente de Concurrencia:** La gestión hotelera requiere evitar condiciones de carrera (double-booking). Un monolito conectado directamente a una base de datos relacional robusta permite transacciones atómicas rápidas sin latencias externas de red distribuidas.
*   **Despliegue Homogéneo y Ligero:** Utilizar contenedores **Docker** permite empaquetar toda la aplicación para garantizar que el sistema funcione de manera idéntica en el entorno de desarrollo y en el servidor de producción, reduciendo fallos por diferencias de sistema operativo o variables locales.
*   **Agilidad de Desarrollo:** La combinación de FastAPI y React proporciona una excelente experiencia de desarrollo (Developer Experience). FastAPI autogenera la documentación Swagger de la API, facilitando que el frontend consuma los endpoints de manera precisa e interactiva.

---

## 2. ¿Cómo? (La Solución Técnica y Arquitectura)

El sistema **BookingSoft** se construye bajo un diseño modular y limpio que divide las responsabilidades en capas lógicas bien definidas:

```text
bookingsoft-monolith/
├── backend/                  (Desarrollado con Python y FastAPI)
│   ├── app/
│   │   ├── main.py           (Punto de entrada de la aplicación FastAPI)
│   │   ├── config/           (Configuración global y variables de entorno)
│   │   ├── api/              (CAPA 1: Controladores / Rutas REST - endpoints JSON)
│   │   ├── services/         (CAPA 2: Lógica de negocio y validación de reglas)
│   │   ├── models/           (Modelos de datos y mapeo relacional SQLAlchemy)
│   │   └── schemas/          (CAPA 3: Validaciones Pydantic para Requests/Responses)
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/                 (Desarrollado con React y JavaScript)
│   ├── src/
│   │   ├── components/       (Componentes visuales y reutilizables)
│   │   ├── context/          (Manejo del estado global de la aplicación)
│   │   └── App.jsx           (Lógica principal de navegación y vistas)
│   ├── Dockerfile
│   └── package.json
│
└── docker-compose.yml        (Orquestación del stack: Backend, Frontend y PostgreSQL)
```

### Detalle de las Capas del Monolito
1.  **Capa de Presentación (Controladores / API endpoints):** Desarrollada con **FastAPI**. Recibe las solicitudes HTTP del cliente React en formato JSON, realiza validaciones sintácticas con esquemas Pydantic y enruta las solicitudes a la capa de servicios.
2.  **Capa de Lógica de Negocio (Servicios):** Implementa las reglas del hotel, tales como: cálculo de penalidades por cancelación, filtros de disponibilidad en rangos de fechas, validación de permisos de acceso según roles y el bloqueo inmediato de habitaciones.
3.  **Capa de Acceso a Datos (Persistencia / Repositorios):** Realiza operaciones de lectura/escritura en la base de datos **PostgreSQL**. Se apoya en un ORM para mapear los objetos de Python a tablas relacionales de forma segura, garantizando la consistencia transaccional.

---

## 3. ¿Para qué? (Objetivos y Beneficios)

El desarrollo e implementación de BookingSoft persigue objetivos estratégicos enfocados tanto en la excelencia operativa de Facile como en las buenas prácticas de desarrollo de software:

### Objetivos Operativos (Negocio)
*   **Garantizar Cero Condiciones de Carrera:** Asegurar que dos solicitudes concurrentes para reservar la misma unidad en la misma fecha sean manejadas de forma que la primera bloquee la fila en la base de datos inmediatamente y la segunda sea notificada de la no disponibilidad.
*   **Disponibilidad 24/7:** Mantener el sistema activo ininterrumpidamente para soportar los turnos continuos del hotel, operando sobre un stack tecnológico ligero que consume pocos recursos.
*   **Control de Acceso Riguroso:** Proteger la información sensible mediante cifrado de contraseñas con **bcrypt** y validación de permisos en base al rol asignado (Recepcionista, Ama de Llaves, Mantenimiento, Conserje), asegurando que cada usuario vea únicamente su panel correspondiente.

### Objetivos Técnicos (Ingeniería)
*   **Integración Ágil y Documentada:** Facilitar la comunicación frontend-backend en tiempo real mediante respuestas JSON rápidas y la documentación de la API generada automáticamente con Swagger (OpenAPI).
*   **Portabilidad y Escalabilidad Futura:** Diseñar el código de manera modular y contenerizada mediante **Docker**, facilitando migraciones, actualizaciones de infraestructura o adición de nuevas funcionalidades en el futuro sin comprometer la estabilidad del sistema.
