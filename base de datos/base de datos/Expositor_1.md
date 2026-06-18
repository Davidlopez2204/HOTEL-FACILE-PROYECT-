# EXPOSITOR 1 — Introducción + Estructura de Tablas (Módulos 1 al 4)

---

## INTRODUCCIÓN

La base de datos **Hotel** fue diseñada para gestionar de forma integral las operaciones de un hotel. Abarca desde el control de acceso de usuarios internos, la gestión de clientes y habitaciones, hasta la facturación, servicios adicionales y eventos. Está compuesta por **22 tablas** organizadas en **8 módulos funcionales**.

Los 8 módulos son:
1. Seguridad y Usuarios
2. Clientes
3. Gestión de Habitaciones
4. Reservas y Estadías
5. Limpieza
6. Facturación y Pagos
7. Servicios y Eventos
8. Configuración

---

## MÓDULO 1: SEGURIDAD Y USUARIOS

### Tabla: `rol`
| Columna     | Tipo de Dato  | Restricción                  |
|-------------|---------------|------------------------------|
| id          | INT           | PRIMARY KEY, AUTO_INCREMENT  |
| nombre      | VARCHAR(50)   | NOT NULL, UNIQUE             |
| descripcion | TEXT          | —                            |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Define los roles del sistema (administrador, recepcionista, limpieza, etc.). Sin esta tabla no se podría controlar qué puede hacer cada usuario dentro del sistema. Es la base del control de acceso.

---

### Tabla: `usuario`
| Columna              | Tipo de Dato   | Restricción                              |
|----------------------|----------------|------------------------------------------|
| id                   | INT            | PRIMARY KEY, AUTO_INCREMENT              |
| nombre               | VARCHAR(100)   | NOT NULL                                 |
| apellido             | VARCHAR(100)   | NOT NULL                                 |
| cedula               | VARCHAR(20)    | NOT NULL, UNIQUE                         |
| email                | VARCHAR(150)   | NOT NULL, UNIQUE                         |
| password             | VARCHAR(255)   | NOT NULL                                 |
| activo               | BOOLEAN        | DEFAULT TRUE                             |
| ultimo_login         | TIMESTAMP      | NULL                                     |
| fecha_creacion       | TIMESTAMP      | DEFAULT CURRENT_TIMESTAMP                |
| fecha_actualizacion  | TIMESTAMP      | DEFAULT CURRENT_TIMESTAMP ON UPDATE      |
| rol_id               | INT            | FOREIGN KEY → rol(id)                    |

- **Llave primaria:** `id`
- **Llaves foráneas:** `rol_id` → `rol(id)`
- **Importancia:** Almacena la información de los empleados que operan el sistema. Cada usuario tiene un rol asignado que determina sus permisos. Permite rastrear quién realizó cada operación y cuándo fue su último acceso.

---

### Tabla: `auditoria`
| Columna    | Tipo de Dato  | Restricción                                  |
|------------|---------------|----------------------------------------------|
| id         | INT           | PRIMARY KEY, AUTO_INCREMENT                  |
| usuario_id | INT           | FOREIGN KEY → usuario(id) ON DELETE SET NULL |
| accion     | VARCHAR(50)   | NOT NULL                                     |
| entidad    | VARCHAR(100)  | NOT NULL                                     |
| entidad_id | INT           | —                                            |
| detalle    | TEXT          | —                                            |
| ip_address | VARCHAR(45)   | —                                            |
| fecha      | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP                    |

- **Llave primaria:** `id`
- **Llaves foráneas:** `usuario_id` → `usuario(id)`
- **Importancia:** Registra un historial de todas las acciones realizadas en el sistema (crear, modificar, eliminar). Es fundamental para la seguridad y trazabilidad. Si ocurre un error o fraude, esta tabla permite identificar quién, qué y cuándo se hizo.

---

## MÓDULO 2: CLIENTES

### Tabla: `tipo_documento`
| Columna | Tipo de Dato | Restricción                  |
|---------|-------------|------------------------------|
| id      | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| nombre  | VARCHAR(50) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Cataloga los tipos de documento de identidad (cédula, pasaporte, RIF, etc.). Permite clasificar correctamente la identificación de cada cliente, algo necesario para cumplir con regulaciones legales y migratorias.

---

### Tabla: `cliente`
| Columna           | Tipo de Dato  | Restricción                      |
|-------------------|---------------|----------------------------------|
| id                | INT           | PRIMARY KEY, AUTO_INCREMENT      |
| nombre            | VARCHAR(100)  | NOT NULL                         |
| apellido          | VARCHAR(100)  | NOT NULL                         |
| identificacion    | VARCHAR(100)  | NOT NULL, UNIQUE                 |
| telefono          | VARCHAR(100)  | —                                |
| email             | VARCHAR(150)  | —                                |
| nacionalidad      | VARCHAR(100)  | —                                |
| fecha_nacimiento  | DATE          | —                                |
| fecha_registro    | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP        |
| tipo_documento_id | INT           | FOREIGN KEY → tipo_documento(id) |

- **Llave primaria:** `id`
- **Llaves foráneas:** `tipo_documento_id` → `tipo_documento(id)`
- **Importancia:** Es la tabla central del negocio. Almacena todos los datos de los huéspedes. Sin clientes registrados no se pueden hacer reservas, facturar ni generar estadísticas de ocupación.

---

### Tabla: `historial_cliente`
| Columna     | Tipo de Dato | Restricción                 |
|-------------|-------------|-----------------------------|
| id          | INT         | PRIMARY KEY, AUTO_INCREMENT |
| cliente_id  | INT         | FOREIGN KEY → cliente(id)   |
| usuario_id  | INT         | FOREIGN KEY → usuario(id)   |
| observacion | TEXT        | NOT NULL                    |
| fecha       | TIMESTAMP   | DEFAULT CURRENT_TIMESTAMP   |

- **Llave primaria:** `id`
- **Llaves foráneas:** `cliente_id` → `cliente(id)`, `usuario_id` → `usuario(id)`
- **Importancia:** Permite registrar notas y observaciones sobre un cliente (preferencias, incidentes, solicitudes especiales). Esto mejora la atención personalizada y ayuda a anticipar necesidades en futuras visitas.

---

## MÓDULO 3: GESTIÓN DE HABITACIONES

### Tabla: `tipo_unidad`
| Columna | Tipo de Dato  | Restricción                  |
|---------|--------------|------------------------------|
| id      | INT          | PRIMARY KEY, AUTO_INCREMENT  |
| nombre  | VARCHAR(100) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Clasifica las habitaciones por tipo (individual, doble, suite, presidencial). Es esencial para asignar tarifas diferenciadas y para que el cliente pueda elegir según sus necesidades.

---

### Tabla: `estado_unidad`
| Columna | Tipo de Dato | Restricción                  |
|---------|-------------|------------------------------|
| id      | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| nombre  | VARCHAR(25) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Define los estados posibles de una habitación (disponible, ocupada, en mantenimiento, en limpieza). Permite saber en tiempo real qué habitaciones están listas para asignar.

---

### Tabla: `habitacion`
| Columna          | Tipo de Dato | Restricción                     |
|------------------|-------------|---------------------------------|
| id               | INT         | PRIMARY KEY, AUTO_INCREMENT     |
| numero           | VARCHAR(10) | NOT NULL, UNIQUE                |
| piso             | INT         | NOT NULL                        |
| capacidad        | INT         | NOT NULL                        |
| descripcion      | TEXT        | —                               |
| tipo_unidad_id   | INT         | FOREIGN KEY → tipo_unidad(id)   |
| estado_unidad_id | INT         | FOREIGN KEY → estado_unidad(id) |

- **Llave primaria:** `id`
- **Llaves foráneas:** `tipo_unidad_id` → `tipo_unidad(id)`, `estado_unidad_id` → `estado_unidad(id)`
- **Importancia:** Representa el inventario físico del hotel. Cada habitación tiene su número, piso, capacidad, tipo y estado actual. Esta información es fundamental para el proceso de check-in/check-out y la asignación de reservas.

---

### Tabla: `tarifa`
| Columna        | Tipo de Dato   | Restricción                   |
|----------------|----------------|-------------------------------|
| id             | INT            | PRIMARY KEY, AUTO_INCREMENT   |
| temporadas     | VARCHAR(100)   | —                             |
| precio         | DECIMAL(10,2)  | NOT NULL                      |
| fecha_inicio   | DATE           | —                             |
| fecha_fin      | DATE           | —                             |
| tipo_unidad_id | INT            | FOREIGN KEY → tipo_unidad(id) |

- **Llave primaria:** `id`
- **Llaves foráneas:** `tipo_unidad_id` → `tipo_unidad(id)`
- **Importancia:** Define los precios por tipo de habitación según la temporada (alta, baja, feriados). Permite aplicar precios dinámicos y generar facturación correcta según el periodo de la estadía.

---

## MÓDULO 4: RESERVAS Y ESTADÍAS

### Tabla: `estado_reserva`
| Columna | Tipo de Dato | Restricción                  |
|---------|-------------|------------------------------|
| id      | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| estado  | VARCHAR(50) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Cataloga los posibles estados de una reserva (confirmada, pendiente, cancelada, completada). Esto permite filtrar y gestionar reservas según su situación actual.

---

### Tabla: `reserva`
| Columna           | Tipo de Dato   | Restricción                      |
|-------------------|----------------|----------------------------------|
| id                | INT            | PRIMARY KEY, AUTO_INCREMENT      |
| cliente_id        | INT            | FOREIGN KEY → cliente(id)        |
| habitacion_id     | INT            | FOREIGN KEY → habitacion(id)     |
| tarifa_id         | INT            | FOREIGN KEY → tarifa(id)         |
| estado_reserva_id | INT            | FOREIGN KEY → estado_reserva(id) |
| fecha_inicio      | DATE           | NOT NULL                         |
| fecha_fin         | DATE           | NOT NULL                         |
| cantidad          | INT            | —                                |
| observaciones     | TEXT           | —                                |
| checkin           | TIMESTAMP      | NULL                             |
| checkout          | TIMESTAMP      | NULL                             |
| estado            | VARCHAR(20)    | DEFAULT 'ACTIVO'                 |
| fecha_creacion    | TIMESTAMP      | DEFAULT CURRENT_TIMESTAMP        |

- **Llave primaria:** `id`
- **Llaves foráneas:** `cliente_id`, `habitacion_id`, `tarifa_id`, `estado_reserva_id`
- **Importancia:** Es una de las tablas más importantes del sistema. Vincula al cliente con una habitación y una tarifa en un rango de fechas específico. Todo el flujo operativo del hotel gira en torno a las reservas.

---

### Tabla: `estadia`
| Columna              | Tipo de Dato | Restricción                  |
|----------------------|-------------|------------------------------|
| id                   | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| reserva_id           | INT         | FOREIGN KEY → reserva(id)    |
| usuario_checkin_id   | INT         | FOREIGN KEY → usuario(id)    |
| usuario_checkout_id  | INT         | FOREIGN KEY → usuario(id)    |
| fecha_checkin        | TIMESTAMP   | DEFAULT CURRENT_TIMESTAMP    |
| fecha_checkout       | TIMESTAMP   | NULL                         |
| estado               | VARCHAR(20) | DEFAULT 'ACTIVO'             |

- **Llave primaria:** `id`
- **Llaves foráneas:** `reserva_id`, `usuario_checkin_id`, `usuario_checkout_id`
- **Importancia:** Registra el periodo real de permanencia del huésped. Diferencia entre la reserva (lo planificado) y la estadía (lo que realmente ocurrió). Permite saber qué recepcionista realizó el check-in y check-out.
