# EXPOSICIÓN — BASE DE DATOS: Hotel

## Distribución de Expositores

| Expositor | Tema Asignado |
|-----------|---------------|
| **ashley xiomara** | Introducción + Estructura de tablas (Módulos 1 al 4) |
| **sebastian parada** | Estructura de tablas (Módulos 5 al 8) + Diagrama de relaciones |
| **todos** | Procedimientos de inserción (INSERT) y relevancia de los datos |
| **jose chico y david lopez** | Procedimientos de actualización (UPDATE) y borrado (DELETE) |
| **maicol mayor** | 10 Consultas SELECT con operadores avanzados + Conclusión |

---

---

# 👤 ashley xiomara — Introducción + Estructura de Tablas (Módulos 1 al 4)

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
- **Importancia:** Clasifica las habitaciones por tipo (habitacion, sencilla, duplex, familiar). Es esencial para asignar tarifas diferenciadas y para que el cliente pueda elegir según sus necesidades.

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

---

---

# 👤 sebastian parada — Estructura de Tablas (Módulos 5 al 8) + Diagrama de Relaciones

## MÓDULO 5: LIMPIEZA

### Tabla: `limpieza`
| Columna       | Tipo de Dato | Restricción                  |
|---------------|-------------|------------------------------|
| id            | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| habitacion_id | INT         | FOREIGN KEY → habitacion(id) |
| usuario_id    | INT         | FOREIGN KEY → usuario(id)    |
| fecha         | TIMESTAMP   | DEFAULT CURRENT_TIMESTAMP    |
| estado        | VARCHAR(20) | NOT NULL                     |
| observacion   | TEXT        | —                            |

- **Llave primaria:** `id`
- **Llaves foráneas:** `habitacion_id` → `habitacion(id)`, `usuario_id` → `usuario(id)`
- **Importancia:** Controla el proceso de limpieza de las habitaciones. Registra quién limpió, cuándo y en qué estado quedó. Esto es clave para garantizar la calidad del servicio y coordinar la disponibilidad de habitaciones.

---

## MÓDULO 6: FACTURACIÓN Y PAGOS

### Tabla: `factura`
| Columna    | Tipo de Dato   | Restricción                  |
|------------|----------------|------------------------------|
| id         | INT            | PRIMARY KEY, AUTO_INCREMENT  |
| cliente_id | INT            | FOREIGN KEY → cliente(id)    |
| reserva_id | INT            | FOREIGN KEY → reserva(id)    |
| descuento  | DECIMAL(10,2)  | DEFAULT 0                    |
| total      | DECIMAL(10,2)  | NOT NULL, DEFAULT 0          |
| fecha      | TIMESTAMP      | DEFAULT CURRENT_TIMESTAMP    |

- **Llave primaria:** `id`
- **Llaves foráneas:** `cliente_id` → `cliente(id)`, `reserva_id` → `reserva(id)`
- **Importancia:** Registra el documento fiscal de cada estadía. Vincula la reserva con el monto a cobrar, incluyendo posibles descuentos. Es esencial para la contabilidad y reportes financieros del hotel.

---

### Tabla: `pago`
| Columna         | Tipo de Dato                               | Restricción                  |
|-----------------|--------------------------------------------|------------------------------|
| id              | INT                                        | PRIMARY KEY, AUTO_INCREMENT  |
| factura_id      | INT                                        | FOREIGN KEY → factura(id)    |
| usuario_id      | INT                                        | FOREIGN KEY → usuario(id)    |
| monto           | DECIMAL(10,2)                              | NOT NULL                     |
| referencia_pago | VARCHAR(100)                               | —                            |
| fecha           | TIMESTAMP                                  | DEFAULT CURRENT_TIMESTAMP    |
| tipo_pago       | ENUM('digital','efectivo')                 | —                            |
| estado_pago     | ENUM('pendiente','completado','cancelado') | DEFAULT 'pendiente'          |

- **Llave primaria:** `id`
- **Llaves foráneas:** `factura_id` → `factura(id)`, `usuario_id` → `usuario(id)`
- **Importancia:** Registra cada pago asociado a una factura. Permite manejar pagos parciales, diferentes métodos de pago y rastrear el estado de cada transacción. Es la tabla que cierra el ciclo financiero.

---

## MÓDULO 7: SERVICIOS Y EVENTOS

### Tabla: `tipo_servicio`
| Columna | Tipo de Dato | Restricción                  |
|---------|-------------|------------------------------|
| id      | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| nombre  | VARCHAR(50) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Clasifica los servicios del hotel por categoría (restaurante, spa, lavandería, minibar). Permite organizar la oferta de servicios adicionales.

---

### Tabla: `servicio`
| Columna          | Tipo de Dato   | Restricción                     |
|------------------|----------------|---------------------------------|
| id               | INT            | PRIMARY KEY, AUTO_INCREMENT     |
| nombre           | VARCHAR(100)   | NOT NULL                        |
| tipo_servicio_id | INT            | FOREIGN KEY → tipo_servicio(id) |
| precio_base      | DECIMAL(10,2)  | —                               |
| activo           | BOOLEAN        | DEFAULT TRUE                    |

- **Llave primaria:** `id`
- **Llaves foráneas:** `tipo_servicio_id` → `tipo_servicio(id)`
- **Importancia:** Almacena el catálogo de servicios disponibles con su precio. Permite activar o desactivar servicios según la temporada o disponibilidad.

---

### Tabla: `consumo_servicio`
| Columna     | Tipo de Dato   | Restricción                  |
|-------------|----------------|------------------------------|
| id          | INT            | PRIMARY KEY, AUTO_INCREMENT  |
| cliente_id  | INT            | FOREIGN KEY → cliente(id)    |
| servicio_id | INT            | FOREIGN KEY → servicio(id)   |
| factura_id  | INT            | FOREIGN KEY → factura(id)    |
| cantidad    | DECIMAL(10,2)  | DEFAULT 1                    |
| observacion | TEXT           | —                            |
| fecha       | TIMESTAMP      | DEFAULT CURRENT_TIMESTAMP    |

- **Llave primaria:** `id`
- **Llaves foráneas:** `cliente_id`, `servicio_id`, `factura_id`
- **Importancia:** Registra cada vez que un cliente consume un servicio adicional. Vincula el consumo a una factura para que pueda cobrarse. Permite analizar qué servicios son los más demandados.

---

### Tabla: `estado_evento`
| Columna | Tipo de Dato | Restricción                  |
|---------|-------------|------------------------------|
| id      | INT         | PRIMARY KEY, AUTO_INCREMENT  |
| nombre  | VARCHAR(50) | NOT NULL, UNIQUE             |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Define los estados posibles de un evento (programado, en curso, finalizado, cancelado). Permite gestionar el ciclo de vida de los eventos del hotel.

---

### Tabla: `evento`
| Columna           | Tipo de Dato   | Restricción                      |
|-------------------|----------------|----------------------------------|
| id                | INT            | PRIMARY KEY, AUTO_INCREMENT      |
| nombre            | VARCHAR(150)   | NOT NULL                         |
| cliente_id        | INT            | FOREIGN KEY → cliente(id)        |
| estado_evento_id  | INT            | FOREIGN KEY → estado_evento(id)  |
| tipo_evento       | VARCHAR(100)   | —                                |
| fecha             | DATE           | NOT NULL                         |
| hora_inicio       | TIME           | —                                |
| hora_fin          | TIME           | —                                |
| cantidad_personas | INT            | —                                |
| precio            | DECIMAL(10,2)  | —                                |
| observaciones     | TEXT           | —                                |

- **Llave primaria:** `id`
- **Llaves foráneas:** `cliente_id` → `cliente(id)`, `estado_evento_id` → `estado_evento(id)`
- **Importancia:** Gestiona eventos organizados en el hotel (bodas, conferencias, fiestas). Registra horarios, asistentes y costos. Es una fuente de ingreso adicional para el hotel.

---

## MÓDULO 8: CONFIGURACIÓN

### Tabla: `configuracion`
| Columna     | Tipo de Dato  | Restricción                  |
|-------------|---------------|------------------------------|
| id          | INT           | PRIMARY KEY, AUTO_INCREMENT  |
| clave       | VARCHAR(50)   | NOT NULL, UNIQUE             |
| valor       | VARCHAR(255)  | NOT NULL                     |
| descripcion | TEXT          | —                            |

- **Llave primaria:** `id`
- **Llaves foráneas:** Ninguna
- **Importancia:** Almacena parámetros generales del sistema (nombre del hotel, IVA, moneda, hora de checkout, etc.). Permite modificar el comportamiento del sistema sin tocar el código fuente.

---

## DIAGRAMA DE RELACIONES ENTRE TABLAS

```
rol ──────────────────┐
                      ▼
usuario ─────────── auditoria
  │
  ├──── historial_cliente ◄── cliente ◄── tipo_documento
  │                              │
  ├──── estadia ◄── reserva ─────┤
  │                    │         │
  │                    ▼         │
  ├──── limpieza ◄── habitacion  │
  │                    │         │
  │              tipo_unidad     │
  │              estado_unidad   │
  │                              │
  ├──── pago ◄── factura ────────┘
  │                 │
  │         consumo_servicio ◄── servicio ◄── tipo_servicio
  │
  └──── evento ◄── estado_evento
                    tarifa ◄── tipo_unidad
                    configuracion (independiente)
```

**Resumen:** La base de datos tiene **22 tablas** conectadas mediante **llaves foráneas** que garantizan la integridad referencial. La tabla `usuario` es la más conectada ya que participa en auditoría, estadías, limpieza, pagos e historial. La tabla `cliente` es la más referenciada por el lado del negocio.

---

---

# 👤 TODOS — Procedimientos de Inserción (INSERT) y Relevancia

## ¿Qué es un INSERT?

El comando `INSERT INTO` se utiliza para agregar nuevos registros a una tabla. Es el primer paso después de crear las tablas: poblarlas con datos.

---

### 3.1 Inserción de Roles
```sql
INSERT INTO rol (nombre, descripcion) VALUES
('Administrador', 'Acceso total al sistema'),
('Recepcionista', 'Gestión de reservas y check-in/check-out'),
('Limpieza', 'Registro de limpieza de habitaciones'),
('Gerente', 'Supervisión general y reportes');
```
**Relevancia:** Se definen los 4 roles base que determinan los permisos de cada usuario. Sin roles no se puede controlar el acceso al sistema. Por ejemplo, un usuario con rol "Limpieza" no debería poder crear facturas.

---

### 3.2 Inserción de Usuarios
```sql
INSERT INTO usuario (nombre, apellido, cedula, email, password, rol_id) VALUES
('Carlos', 'Mendoza', 'V-12345678', 'carlos@hotel.com', SHA2('admin123', 256), 1),
('María', 'López', 'V-23456789', 'maria@hotel.com', SHA2('recep456', 256), 2),
('José', 'Ramírez', 'V-34567890', 'jose@hotel.com', SHA2('limp789', 256), 3),
('Ana', 'García', 'V-45678901', 'ana@hotel.com', SHA2('ger321', 256), 4);
```
**Relevancia:** Se crean los 4 empleados del hotel. Las contraseñas se encriptan con `SHA2` (función de hash de 256 bits) por seguridad: nunca se almacenan en texto plano. Cada usuario está vinculado a un `rol_id` específico.

---

### 3.3 Inserción de Tipos de Documento
```sql
INSERT INTO tipo_documento (nombre) VALUES
('Cédula de Identidad'),
('Pasaporte'),
('RIF'),
('Licencia de Conducir');
```
**Relevancia:** Se catalogan los 4 tipos de identificación que puede presentar un cliente. Es un requisito legal para hoteles registrar el tipo y número de documento del huésped.

---

### 3.4 Inserción de Clientes
```sql
INSERT INTO cliente (nombre, apellido, identificacion, telefono, email, 
                     nacionalidad, fecha_nacimiento, tipo_documento_id) VALUES
('Pedro', 'Martínez', 'V-11111111', '0412-1234567', 'pedro@gmail.com', 
 'Venezolano', '1990-05-15', 1),
('Laura', 'Fernández', 'E-22222222', '0414-7654321', 'laura@gmail.com', 
 'Colombiana', '1985-08-22', 2),
('Miguel', 'Torres', 'V-33333333', '0416-9876543', 'miguel@gmail.com', 
 'Venezolano', '1978-12-01', 1),
('Sofía', 'Rojas', 'V-44444444', '0424-1112233', NULL, 
 'Venezolana', '1995-03-10', 1),
('Ricardo', 'Díaz', 'E-55555555', '0412-4455667', 'ricardo@gmail.com', 
 'Ecuatoriano', NULL, 2);
```
**Relevancia:** Se registran 5 huéspedes con datos variados. Noten que **Sofía no tiene email** (NULL) y **Ricardo no tiene fecha de nacimiento** (NULL). Esto simula un escenario real donde no toda la información está siempre disponible. La columna `email` no tiene restricción NOT NULL precisamente para permitir esto.

---

### 3.5 Inserción de Historial de Clientes
```sql
INSERT INTO historial_cliente (cliente_id, usuario_id, observacion) VALUES
(1, 2, 'Cliente VIP, siempre solicita habitación en piso bajo'),
(2, 2, 'Alérgica al maní, informar a restaurante'),
(3, 1, 'Solicitó factura con datos fiscales especiales');
```
**Relevancia:** Se registran notas importantes sobre los clientes. Por ejemplo, saber que Laura es alérgica al maní es información crítica para el restaurante del hotel.

---

### 3.6 Inserción de Tipos de Unidad, Estados y Habitaciones
```sql
INSERT INTO tipo_unidad (nombre) VALUES
('Individual'), ('Doble'), ('Suite'), ('Presidencial'), ('Familiar');

INSERT INTO estado_unidad (nombre) VALUES
('Disponible'), ('Ocupada'), ('Mantenimiento'), ('Limpieza');

INSERT INTO habitacion (numero, piso, capacidad, descripcion, 
                        tipo_unidad_id, estado_unidad_id) VALUES
('101', 1, 1, 'Habitación individual con vista al jardín', 1, 1),
('102', 1, 2, 'Habitación doble estándar', 2, 1),
('201', 2, 2, 'Suite con jacuzzi', 3, 2),
('202', 2, 4, 'Habitación familiar amplia', 5, 1),
('301', 3, 2, 'Suite presidencial con terraza', 4, 3),
('302', 3, 1, 'Individual en piso superior', 1, 4);
```
**Relevancia:** Se registra el inventario de 6 habitaciones en 3 pisos con diferentes tipos y estados. Las habitaciones 201 (ocupada), 301 (mantenimiento) y 302 (en limpieza) no están disponibles, lo cual refleja un escenario operativo real.

---

### 3.7 Inserción de Tarifas
```sql
INSERT INTO tarifa (temporadas, precio, fecha_inicio, fecha_fin, tipo_unidad_id) VALUES
('Temporada Baja', 50.00, '2026-01-01', '2026-03-31', 1),
('Temporada Baja', 80.00, '2026-01-01', '2026-03-31', 2),
('Temporada Alta', 120.00, '2026-07-01', '2026-09-30', 3),
('Temporada Alta', 250.00, '2026-07-01', '2026-09-30', 4),
('Temporada Media', 100.00, '2026-04-01', '2026-06-30', 5);
```
**Relevancia:** Se definen 5 tarifas que combinan temporada + tipo de habitación. Por ejemplo, una Suite en temporada alta cuesta $120/noche mientras que una Individual en temporada baja cuesta $50/noche.

---

### 3.8 Inserción de Reservas y Estadías
```sql
INSERT INTO estado_reserva (estado) VALUES
('Confirmada'), ('Pendiente'), ('Cancelada'), ('Completada');

INSERT INTO reserva (cliente_id, habitacion_id, tarifa_id, estado_reserva_id, 
                     fecha_inicio, fecha_fin, cantidad, observaciones) VALUES
(1, 1, 1, 1, '2026-04-15', '2026-04-18', 1, 'Cliente frecuente, prefiere piso bajo'),
(2, 3, 3, 1, '2026-07-10', '2026-07-15', 2, 'Luna de miel'),
(3, 2, 2, 2, '2026-05-01', '2026-05-03', 2, NULL),
(4, 4, 5, 1, '2026-04-20', '2026-04-25', 4, 'Viaje familiar con niños'),
(5, 1, 1, 3, '2026-03-10', '2026-03-12', 1, 'Cancelada por el cliente');

INSERT INTO estadia (reserva_id, usuario_checkin_id, usuario_checkout_id, 
                     fecha_checkin, fecha_checkout, estado) VALUES
(1, 2, 2, '2026-04-15 14:00:00', '2026-04-18 11:00:00', 'COMPLETADO'),
(2, 2, NULL, '2026-07-10 15:30:00', NULL, 'ACTIVO');
```
**Relevancia:** Se crean 5 reservas en diferentes estados y 2 estadías. La reserva 5 fue cancelada. La estadía 1 ya se completó pero la estadía 2 está activa (el huésped aún no ha hecho checkout, por eso `fecha_checkout` y `usuario_checkout_id` son NULL).

---

### 3.9 Inserción de Facturación, Pagos, Servicios y Eventos
```sql
INSERT INTO factura (cliente_id, reserva_id, descuento, total) VALUES
(1, 1, 10.00, 140.00),
(2, 2, 0.00, 600.00),
(4, 4, 25.00, 475.00);

INSERT INTO pago (factura_id, usuario_id, monto, referencia_pago, tipo_pago, estado_pago) VALUES
(1, 2, 140.00, 'REF-001-2026', 'efectivo', 'completado'),
(2, 2, 300.00, 'REF-002-2026', 'digital', 'completado'),
(2, 2, 300.00, 'REF-003-2026', 'digital', 'pendiente'),
(3, 2, 475.00, NULL, 'efectivo', 'pendiente');

INSERT INTO tipo_servicio (nombre) VALUES
('Restaurante'), ('Spa'), ('Lavandería'), ('Minibar'), ('Transporte');

INSERT INTO servicio (nombre, tipo_servicio_id, precio_base) VALUES
('Desayuno Buffet', 1, 15.00),
('Masaje Relajante', 2, 45.00),
('Lavado y Planchado', 3, 10.00),
('Minibar Premium', 4, 25.00),
('Transfer Aeropuerto', 5, 35.00);

INSERT INTO consumo_servicio (cliente_id, servicio_id, factura_id, cantidad, observacion) VALUES
(1, 1, 1, 3, 'Desayuno para 3 días'),
(1, 3, 1, 1, 'Lavado de traje'),
(2, 2, 2, 2, 'Masaje para pareja'),
(4, 1, 3, 5, 'Desayuno familiar 5 días');

INSERT INTO estado_evento (nombre) VALUES
('Programado'), ('En Curso'), ('Finalizado'), ('Cancelado');

INSERT INTO evento (nombre, cliente_id, estado_evento_id, tipo_evento, fecha, 
                    hora_inicio, hora_fin, cantidad_personas, precio, observaciones) VALUES
('Boda Martínez-López', 1, 1, 'Boda', '2026-06-15', '18:00:00', '23:00:00', 150, 5000.00, 
 'Decoración floral incluida'),
('Conferencia TechVzla', 3, 1, 'Conferencia', '2026-05-20', '09:00:00', '17:00:00', 80, 2000.00, NULL);

INSERT INTO configuracion (clave, valor, descripcion) VALUES
('nombre_hotel', 'Hotel Gran Venezuela', 'Nombre comercial del hotel'),
('iva', '16', 'Porcentaje de IVA aplicable'),
('moneda', 'USD', 'Moneda principal de operación'),
('hora_checkout', '12:00', 'Hora límite de checkout'),
('max_reservas_dia', '50', 'Máximo de reservas por día');

INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, detalle, ip_address) VALUES
(1, 'INSERT', 'reserva', 1, 'Nueva reserva creada para Pedro Martínez', '192.168.1.10'),
(2, 'UPDATE', 'habitacion', 1, 'Estado cambiado a Ocupada', '192.168.1.15'),
(1, 'DELETE', 'reserva', 5, 'Reserva cancelada por solicitud del cliente', '192.168.1.10');
```
**Relevancia:** Se completa todo el ecosistema de datos: facturas con y sin descuento, pagos en efectivo y digitales (uno parcial), servicios consumidos, eventos programados, configuraciones globales y registros de auditoría.

---

---

# 👤 Jose chico y david lopez  — Procedimientos de Actualización (UPDATE) y Borrado (DELETE)

## ACTUALIZACIONES (UPDATE)

El comando `UPDATE` se utiliza para modificar datos existentes en una tabla. Es fundamental porque los datos cambian constantemente en un sistema hotelero: habitaciones cambian de estado, pagos se completan, empleados se desactivan.

---

### UPDATE 1: Cambiar estado de habitación a "Ocupada" tras check-in
```sql
UPDATE habitacion SET estado_unidad_id = 2 WHERE id = 1;
```
**¿Por qué se ejecuta?** Cuando el huésped Pedro Martínez hace check-in, la habitación 101 pasa de "Disponible" (id=1) a "Ocupada" (id=2). **Esto es esencial** porque evita que el sistema asigne esa misma habitación a otro cliente mientras está en uso. Sin esta actualización se podrían generar conflictos de doble asignación.

---

### UPDATE 2: Registrar el checkout de una estadía
```sql
UPDATE estadia SET 
    fecha_checkout = NOW(), 
    usuario_checkout_id = 2, 
    estado = 'COMPLETADO' 
WHERE id = 2;
```
**¿Por qué se ejecuta?** Cuando Laura Fernández termina su estadía y hace checkout, se actualizan tres campos simultáneamente: la fecha exacta de salida, el empleado que procesó la salida (María, id=2) y el estado cambia a "COMPLETADO". **Esto libera la habitación** y genera el registro completo de la estadía para facturación y estadísticas.

---

### UPDATE 3: Actualizar estado de pago a completado
```sql
UPDATE pago SET estado_pago = 'completado' WHERE id = 3;
```
**¿Por qué se ejecuta?** El pago con id=3 era una transferencia digital de $300 que estaba pendiente de verificación. Una vez confirmada por el banco, el contador actualiza su estado a "completado". **Esto es importante** para que el departamento de contabilidad sepa que el dinero fue efectivamente recibido y la factura se considere saldada.

---

### UPDATE 4: Desactivar un usuario que ya no trabaja en el hotel
```sql
UPDATE usuario SET activo = FALSE WHERE id = 3;
```
**¿Por qué se ejecuta?** José Ramírez (personal de limpieza) ya no trabaja en el hotel. En lugar de borrarlo con DELETE, se desactiva poniendo `activo = FALSE`. **Esto es una buena práctica** porque se mantiene el historial de todas sus acciones pasadas (limpiezas realizadas, registros de auditoría) pero se le impide iniciar sesión nuevamente. A esto se le llama **borrado lógico**.

---

### UPDATE 5: Actualizar precio de una tarifa por inflación
```sql
UPDATE tarifa SET precio = 65.00 WHERE id = 1;
```
**¿Por qué se ejecuta?** La tarifa de "Temporada Baja" para habitaciones individuales subió de $50.00 a $65.00 debido a la inflación o ajustes de mercado. **Es necesario** actualizar el precio para que las nuevas reservas se facturen con la tarifa correcta. Las reservas ya existentes mantienen la tarifa con la que se crearon.

---

## BORRADOS (DELETE)

El comando `DELETE` elimina registros de una tabla permanentemente. Se debe usar con precaución porque los datos eliminados no se pueden recuperar. En un sistema real, es preferible usar "borrado lógico" (como el UPDATE del usuario), pero hay casos donde el DELETE es apropiado.

---

### DELETE 1: Eliminar una reserva cancelada
```sql
DELETE FROM reserva WHERE id = 5 AND estado = 'ACTIVO';
```
**¿Por qué se ejecuta?** La reserva 5 de Ricardo Díaz fue cancelada por el cliente. Se elimina para liberar la relación con la habitación 101. **La condición `AND estado = 'ACTIVO'`** es una capa de seguridad: solo se borra si el estado lo permite, evitando eliminar accidentalmente reservas completadas. En producción, se recomienda un borrado lógico cambiando el estado.

---

### DELETE 2: Eliminar un registro de limpieza incorrecto
```sql
DELETE FROM limpieza WHERE id = 2;
```
**¿Por qué se ejecuta?** El registro de limpieza con id=2 fue creado por error (se registró la habitación equivocada o fue un duplicado). **Es necesario eliminarlo** para mantener la integridad de los reportes de limpieza y evitar que se generen estadísticas incorrectas sobre el rendimiento del personal.

---

### DELETE 3: Eliminar un tipo de servicio descontinuado
```sql
DELETE FROM tipo_servicio WHERE id = 5;
```
**¿Por qué se ejecuta?** El hotel decidió descontinuar el servicio de "Transporte" porque ya no cuenta con vehículos propios. **Antes de ejecutar este DELETE**, se debe verificar que no existan servicios activos vinculados a esta categoría, ya que la llave foránea lo impedirá. Si hay servicios vinculados, primero se deben eliminar o reasignar.

---

### DELETE 4: Eliminar un evento cancelado
```sql
DELETE FROM evento WHERE id = 2 AND estado_evento_id = 4;
```
**¿Por qué se ejecuta?** La "Conferencia TechVzla" fue cancelada definitivamente y el cliente no desea reprogramarla. **La condición `AND estado_evento_id = 4`** (cancelado) asegura que solo se eliminen eventos que ya fueron marcados como cancelados. Esto mantiene la agenda del hotel limpia y actualizada.

---

### DELETE 5: Eliminar configuración obsoleta
```sql
DELETE FROM configuracion WHERE clave = 'max_reservas_dia';
```
**¿Por qué se ejecuta?** El hotel decidió que no necesita limitar el número de reservas diarias, por lo que este parámetro ya no tiene sentido. **Al eliminarlo**, el sistema dejaría de aplicar esa restricción y permitiría reservas ilimitadas por día.

---

## Resumen Comparativo UPDATE vs DELETE

| Aspecto | UPDATE | DELETE |
|---------|--------|--------|
| **Acción** | Modifica datos existentes | Elimina registros completos |
| **Reversibilidad** | Los datos anteriores se pierden (sin backup) | El registro completo desaparece |
| **Uso recomendado** | Cambios de estado, correcciones, actualizaciones | Datos erróneos, registros temporales, limpieza |
| **Buena práctica** | Borrado lógico (activo = FALSE) | Solo cuando no afecte la integridad referencial |

---

---

# 👤 maicol mayor — 10 Consultas SELECT con Operadores Avanzados + Conclusión

## ¿Qué son los operadores avanzados?

| Operador | Función | Ejemplo |
|----------|---------|---------|
| **LIKE** | Busca patrones de texto | `WHERE nombre LIKE 'P%'` (empieza con P) |
| **BETWEEN** | Filtra rangos de valores | `WHERE precio BETWEEN 50 AND 150` |
| **IN** | Compara con una lista de valores | `WHERE estado IN ('activo', 'pendiente')` |
| **IS NULL** | Busca valores vacíos/nulos | `WHERE email IS NULL` |

---

### Consulta 1: Buscar clientes cuyo nombre comience con "P" (LIKE)
```sql
SELECT * FROM cliente WHERE nombre LIKE 'P%';
```
**Relevancia:** Permite buscar rápidamente clientes cuando solo se conoce la inicial del nombre. El símbolo `%` significa "cualquier cantidad de caracteres después de P". Es útil cuando un huésped llama por teléfono y el recepcionista necesita ubicarlo rápidamente.

**Resultado esperado:** Pedro Martínez.

---

### Consulta 2: Buscar reservas del mes de abril (BETWEEN)
```sql
SELECT r.id, c.nombre, c.apellido, r.fecha_inicio, r.fecha_fin 
FROM reserva r 
JOIN cliente c ON r.cliente_id = c.id 
WHERE r.fecha_inicio BETWEEN '2026-04-01' AND '2026-04-30';
```
**Relevancia:** Muestra todas las reservas que inician en abril. El `BETWEEN` incluye ambos extremos (1 de abril y 30 de abril). Esto es esencial para planificar la ocupación del hotel, asignar personal de limpieza y preparar la logística del mes.

**Resultado esperado:** Reservas de Pedro Martínez (15-18 abril) y Sofía Rojas (20-25 abril).

---

### Consulta 3: Buscar habitaciones disponibles o en limpieza (IN)
```sql
SELECT h.numero, h.piso, eu.nombre AS estado 
FROM habitacion h 
JOIN estado_unidad eu ON h.estado_unidad_id = eu.id 
WHERE eu.nombre IN ('Disponible', 'Limpieza');
```
**Relevancia:** El `IN` permite buscar en una lista de valores. Esta consulta muestra las habitaciones que están listas o pronto lo estarán. Las de "Limpieza" están a punto de liberarse. Es información clave para el recepcionista durante el check-in.

**Resultado esperado:** Habitaciones 101, 102, 202 (disponibles) y 302 (en limpieza).

---

### Consulta 4: Buscar clientes sin email registrado (IS NULL)
```sql
SELECT nombre, apellido, identificacion, telefono 
FROM cliente 
WHERE email IS NULL;
```
**Relevancia:** `IS NULL` busca registros donde un campo no tiene valor asignado. No se puede usar `= NULL` (eso no funciona en SQL). Esta consulta identifica clientes que no proporcionaron email, necesario para contactarlos y solicitar este dato para enviar confirmaciones digitales.

**Resultado esperado:** Sofía Rojas.

---

### Consulta 5: Buscar servicios que contengan "Masaje" (LIKE)
```sql
SELECT s.nombre, ts.nombre AS categoria, s.precio_base 
FROM servicio s 
JOIN tipo_servicio ts ON s.tipo_servicio_id = ts.id 
WHERE s.nombre LIKE '%Masaje%';
```
**Relevancia:** El patrón `%Masaje%` busca la palabra "Masaje" en cualquier posición del nombre. `%` al inicio y al final significa "cualquier texto antes y después". Útil cuando un huésped pregunta "¿tienen masajes?" y el recepcionista necesita listar opciones.

**Resultado esperado:** Masaje Relajante — Spa — $45.00.

---

### Consulta 6: Buscar tarifas entre $50 y $150 por noche (BETWEEN)
```sql
SELECT t.temporadas, tu.nombre AS tipo_habitacion, t.precio 
FROM tarifa t 
JOIN tipo_unidad tu ON t.tipo_unidad_id = tu.id 
WHERE t.precio BETWEEN 50.00 AND 150.00;
```
**Relevancia:** Permite filtrar tarifas según el presupuesto del cliente. Si un huésped dice "puedo pagar entre $50 y $150 por noche", esta consulta muestra todas las opciones disponibles dentro de ese rango. El `BETWEEN` con decimales funciona igual que con enteros.

**Resultado esperado:** Individual $50, Doble $80, Familiar $100, Suite $120.

---

### Consulta 7: Buscar pagos pendientes o cancelados (IN)
```sql
SELECT p.id, f.id AS factura, p.monto, p.tipo_pago, p.estado_pago 
FROM pago p 
JOIN factura f ON p.factura_id = f.id 
WHERE p.estado_pago IN ('pendiente', 'cancelado');
```
**Relevancia:** El departamento de contabilidad necesita saber qué pagos aún no se han completado. El `IN` permite buscar múltiples estados a la vez, lo cual es más limpio que escribir `WHERE estado_pago = 'pendiente' OR estado_pago = 'cancelado'`.

**Resultado esperado:** Pago 3 ($300 digital pendiente) y Pago 4 ($475 efectivo pendiente).

---

### Consulta 8: Buscar huéspedes actualmente alojados — sin checkout (IS NULL)
```sql
SELECT e.id, r.id AS reserva, c.nombre, c.apellido, e.fecha_checkin 
FROM estadia e 
JOIN reserva r ON e.reserva_id = r.id 
JOIN cliente c ON r.cliente_id = c.id 
WHERE e.fecha_checkout IS NULL;
```
**Relevancia:** Los huéspedes que aún no han hecho checkout tienen `fecha_checkout = NULL`. Esta consulta muestra la **ocupación actual del hotel en tiempo real**. Es una de las consultas más usadas por la recepción y la gerencia.

**Resultado esperado:** Laura Fernández (check-in: 10 julio 2026, aún alojada).

---

### Consulta 9: Buscar clientes colombianos o ecuatorianos con "a" en el nombre (IN + LIKE)
```sql
SELECT nombre, apellido, nacionalidad, email 
FROM cliente 
WHERE nacionalidad IN ('Colombiana', 'Ecuatoriano') 
AND nombre LIKE '%a%';
```
**Relevancia:** Esta consulta combina **dos operadores**: `IN` para filtrar por múltiples nacionalidades y `LIKE` para buscar un patrón en el nombre. Es útil para campañas de marketing dirigidas a segmentos específicos de clientes o para generar reportes migratorios.

**Resultado esperado:** Laura Fernández (Colombiana) y Ricardo Díaz (Ecuatoriano, la "a" está en Ricardo).

---

### Consulta 10: Buscar eventos tecnológicos entre mayo y julio (BETWEEN + LIKE)
```sql
SELECT e.nombre, e.tipo_evento, e.fecha, e.cantidad_personas, e.precio, 
       ee.nombre AS estado 
FROM evento e 
JOIN estado_evento ee ON e.estado_evento_id = ee.id 
WHERE e.fecha BETWEEN '2026-05-01' AND '2026-07-31' 
AND e.nombre LIKE '%Tech%';
```
**Relevancia:** Combina `BETWEEN` para filtrar por un rango de fechas con `LIKE` para buscar eventos que contengan "Tech" en su nombre. Permite al departamento de eventos planificar logística, personal y recursos para conferencias tecnológicas en ese periodo.

**Resultado esperado:** Conferencia TechVzla — 20 mayo 2026 — 80 personas — $2,000.

---

## RESUMEN DE OPERADORES UTILIZADOS

| # | Consulta | Operador(es) |
|---|----------|--------------|
| 1 | Clientes por inicial | LIKE |
| 2 | Reservas de abril | BETWEEN |
| 3 | Habitaciones por estado | IN |
| 4 | Clientes sin email | IS NULL |
| 5 | Servicios por nombre | LIKE |
| 6 | Tarifas por rango de precio | BETWEEN |
| 7 | Pagos por estado | IN |
| 8 | Huéspedes sin checkout | IS NULL |
| 9 | Clientes por nacionalidad y nombre | IN + LIKE |
| 10 | Eventos por fecha y nombre | BETWEEN + LIKE |

---

## CONCLUSIÓN

La base de datos **Hotel** está diseñada siguiendo los principios de **normalización relacional**. Sus **22 tablas** cubren todos los aspectos operativos de un hotel:

- **Seguridad:** Control de acceso por roles y auditoría de acciones.
- **Clientes:** Registro completo con historial personalizado.
- **Habitaciones:** Inventario con tipos, estados y tarifas dinámicas.
- **Reservas:** Flujo completo desde la reserva hasta el checkout.
- **Limpieza:** Trazabilidad del proceso de limpieza.
- **Facturación:** Gestión de facturas y pagos parciales/totales.
- **Servicios:** Catálogo y registro de consumos adicionales.
- **Eventos:** Gestión de eventos con estados y costos.

El uso de **llaves primarias** garantiza la identificación única de cada registro, mientras que las **llaves foráneas** mantienen la **integridad referencial** entre tablas, asegurando que no existan datos huérfanos en la base de datos.
