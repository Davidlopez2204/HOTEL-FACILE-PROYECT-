# EXPOSITOR 3 — Procedimientos de Inserción (INSERT) y Relevancia

---

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
('Boda Martínez-López', 1, 1, 'Boda', '2026-06-15', '18:00:00', '23:00:00', 
 150, 5000.00, 'Decoración floral incluida'),
('Conferencia TechVzla', 3, 1, 'Conferencia', '2026-05-20', '09:00:00', '17:00:00', 
 80, 2000.00, NULL);

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
