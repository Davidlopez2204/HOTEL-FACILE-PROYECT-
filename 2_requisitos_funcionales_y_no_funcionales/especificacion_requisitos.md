# Requisitos Funcionales y No Funcionales
## Proyecto: Sistema de Gestión Hotelera - Facile

Este documento presenta la especificación formal de los **Requisitos Funcionales (RF)** y **Requisitos No Funcionales (RNF)** para el desarrollo de la plataforma de gestión de Facile.

---

## 1. Requisitos Funcionales (RF)

### Módulo de Usuarios
*   **RF01. Registrar usuario:** El sistema deberá permitir registrar personal y huéspedes dentro de la plataforma.
*   **RF02. Consultar usuarios:** El sistema deberá permitir visualizar el listado de usuarios registrados.
*   **RF03. Consultar usuario específico:** El sistema deberá permitir consultar la información detallada de un usuario por su documento.
*   **RF04. Iniciar sesión:** El sistema deberá permitir la autenticación mediante correo y contraseña.
*   **RF05. Cerrar sesión:** El sistema deberá permitir finalizar la sesión activa.
*   **RF06. Modificar rol:** El sistema deberá permitir al administrador cambiar el rol de un usuario (Recepcionista, Ama de Llaves, Mantenimiento, Conserje).
*   **RF07. Validar credenciales:** El sistema deberá validar correo y contraseña antes de permitir el acceso.
*   **RF08. Cifrar contraseñas:** El sistema deberá almacenar las contraseñas cifradas mediante bcrypt.
*   **RF09. Validar permisos:** El sistema deberá controlar el acceso según el rol asignado (cada rol ve solo sus módulos).
*   **RF10. Gestionar estado del usuario:** El sistema deberá permitir registrar usuarios activos e inactivos.

### Módulo de Reservas
*   **RF11. Crear reserva:** El sistema deberá permitir crear una reserva bloqueando la unidad de inmediato.
*   **RF12. Consultar disponibilidad:** El sistema deberá mostrar en tiempo real qué unidades están disponibles para un rango de fechas.
*   **RF13. Modificar reserva:** El sistema deberá permitir cambiar fechas o datos de una reserva activa.
*   **RF14. Cancelar reserva:** El sistema deberá permitir cancelar una reserva aplicando la política de penalidad correspondiente.
*   **RF15. Reservar Sala de Juntas / Coworking:** El sistema deberá permitir que cualquier persona, hospedada o no, reserve estos espacios por horas.

---

## 2. Requisitos No Funcionales (RNF)

| Código | Requisito No Funcional | Categoría / Descripción |
| :--- | :--- | :--- |
| **RNF01** | La API deberá responder en formato JSON. | **Interfaz e Integración** |
| **RNF02** | La base de datos utilizada será **PostgreSQL**. | **Persistencia de Datos** |
| **RNF03** | El backend será desarrollado con **Python y el framework FastAPI**. | **Tecnología del Servidor** |
| **RNF04** | El frontend será desarrollado con **React y JavaScript**. | **Tecnología del Cliente** |
| **RNF05** | Las contraseñas deberán almacenarse cifradas con bcrypt. | **Seguridad de Datos** |
| **RNF06** | La documentación de la API será generada con Swagger (incluido nativamente en FastAPI). | **Documentación Técnica** |
| **RNF07** | La aplicación deberá ejecutarse en contenedores mediante **Docker** para garantizar consistencia entre entornos. | **Despliegue e Infraestructura** |
| **RNF08** | La aplicación deberá utilizar variables de entorno para la configuración sensible. | **Configuración y Seguridad** |
| **RNF09** | El sistema deberá evitar condiciones de carrera al bloquear unidades concurrentemente. | **Concurrencia e Integridad** |
| **RNF10** | El sistema deberá estar disponible 24/7 (alta disponibilidad). | **Disponibilidad** |
| **RNF11** | El desarrollo se realizará utilizando **Visual Studio Code** y **Antigravity**. | **Herramientas de Desarrollo** |
