# EXPOSITOR 5 — 10 Consultas SELECT con Operadores Avanzados + Conclusión

---

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
