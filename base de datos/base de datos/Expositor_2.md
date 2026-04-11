# EXPOSITOR 2 — Estructura de Tablas (Módulos 5 al 8) + Diagrama de Relaciones

---

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
