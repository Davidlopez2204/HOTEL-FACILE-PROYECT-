-- ============================================================
-- BASE DE DATOS: HOTEL
-- ============================================================

-- 1. SEGURIDAD Y USUARIOS
CREATE DATABASE Hotel;
USE Hotel;

CREATE TABLE rol (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT
);

CREATE TABLE usuario (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    nombre              VARCHAR(100) NOT NULL,
    apellido            VARCHAR(100) NOT NULL,
    cedula              VARCHAR(20) NOT NULL UNIQUE,
    email               VARCHAR(150) NOT NULL UNIQUE,
    password            VARCHAR(255) NOT NULL,
    activo              BOOLEAN DEFAULT TRUE,
    ultimo_login        TIMESTAMP NULL,
    fecha_creacion      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    rol_id              INT,
    FOREIGN KEY (rol_id) REFERENCES rol(id)
);

CREATE TABLE auditoria (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id  INT,
    accion      VARCHAR(50) NOT NULL,
    entidad     VARCHAR(100) NOT NULL,
    entidad_id  INT,
    detalle     TEXT,
    ip_address  VARCHAR(45),
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE SET NULL
);

-- 2. CLIENTES
CREATE TABLE tipo_documento (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE cliente (
    id                INT AUTO_INCREMENT PRIMARY KEY,
    nombre            VARCHAR(100) NOT NULL,
    apellido          VARCHAR(100) NOT NULL,
    identificacion    VARCHAR(100) NOT NULL UNIQUE,
    telefono          VARCHAR(100),
    email             VARCHAR(150),
    nacionalidad      VARCHAR(100),
    fecha_nacimiento  DATE,
    fecha_registro    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_documento_id INT,
    FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento(id)
);

CREATE TABLE historial_cliente (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id  INT,
    usuario_id  INT,
    observacion TEXT NOT NULL,
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- 3. GESTIÓN DE HABITACIONES
CREATE TABLE tipo_unidad (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE estado_unidad (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL UNIQUE
);

CREATE TABLE habitacion (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    numero           VARCHAR(10) NOT NULL UNIQUE,
    piso             INT NOT NULL,
    capacidad        INT NOT NULL,
    descripcion      TEXT,
    tipo_unidad_id   INT,
    estado_unidad_id INT,
    FOREIGN KEY (tipo_unidad_id) REFERENCES tipo_unidad(id),
    FOREIGN KEY (estado_unidad_id) REFERENCES estado_unidad(id)
);

CREATE TABLE tarifa (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    temporadas     VARCHAR(100),
    precio         DECIMAL(10,2) NOT NULL,
    fecha_inicio   DATE,
    fecha_fin      DATE,
    tipo_unidad_id INT,
    FOREIGN KEY (tipo_unidad_id) REFERENCES tipo_unidad(id)
);

-- 4. RESERVAS Y ESTADÍAS
CREATE TABLE estado_reserva (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE reserva (
    id                INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id        INT,
    habitacion_id     INT,
    tarifa_id         INT,
    estado_reserva_id INT,
    fecha_inicio      DATE NOT NULL,
    fecha_fin         DATE NOT NULL,
    cantidad          INT,
    observaciones     TEXT,
    checkin           TIMESTAMP NULL,
    checkout          TIMESTAMP NULL,
    estado            VARCHAR(20) DEFAULT 'ACTIVO',
    fecha_creacion    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (habitacion_id) REFERENCES habitacion(id),
    FOREIGN KEY (tarifa_id) REFERENCES tarifa(id),
    FOREIGN KEY (estado_reserva_id) REFERENCES estado_reserva(id)
);

CREATE TABLE estadia (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    reserva_id          INT,
    usuario_checkin_id  INT,
    usuario_checkout_id INT,
    fecha_checkin       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_checkout      TIMESTAMP NULL,
    estado              VARCHAR(20) DEFAULT 'ACTIVO',
    FOREIGN KEY (reserva_id) REFERENCES reserva(id),
    FOREIGN KEY (usuario_checkin_id) REFERENCES usuario(id),
    FOREIGN KEY (usuario_checkout_id) REFERENCES usuario(id)
);

-- 5. LIMPIEZA
CREATE TABLE limpieza (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    habitacion_id INT,
    usuario_id    INT,
    fecha         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado        VARCHAR(20) NOT NULL,
    observacion   TEXT,
    FOREIGN KEY (habitacion_id) REFERENCES habitacion(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- 6. FACTURACIÓN Y PAGOS
CREATE TABLE factura (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id  INT,
    reserva_id  INT,
    descuento   DECIMAL(10,2) DEFAULT 0,
    total       DECIMAL(10,2) NOT NULL DEFAULT 0,
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (reserva_id) REFERENCES reserva(id)
);

CREATE TABLE pago (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    factura_id      INT,
    usuario_id      INT,
    monto           DECIMAL(10,2) NOT NULL,
    referencia_pago VARCHAR(100),
    fecha           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_pago       ENUM('digital','efectivo'),
    estado_pago     ENUM('pendiente','completado','cancelado') DEFAULT 'pendiente',
    FOREIGN KEY (factura_id) REFERENCES factura(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- 7. SERVICIOS Y EVENTOS
CREATE TABLE tipo_servicio (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE servicio (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    nombre           VARCHAR(100) NOT NULL,
    tipo_servicio_id INT,
    precio_base      DECIMAL(10,2),
    activo           BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (tipo_servicio_id) REFERENCES tipo_servicio(id)
);

CREATE TABLE consumo_servicio (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id  INT,
    servicio_id INT,
    factura_id  INT,
    cantidad    DECIMAL(10,2) DEFAULT 1,
    observacion TEXT,
    fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (servicio_id) REFERENCES servicio(id),
    FOREIGN KEY (factura_id) REFERENCES factura(id)
);

CREATE TABLE estado_evento (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE evento (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    nombre           VARCHAR(150) NOT NULL,
    cliente_id       INT,
    estado_evento_id INT,
    tipo_evento      VARCHAR(100),
    fecha            DATE NOT NULL,
    hora_inicio      TIME,
    hora_fin         TIME,
    cantidad_personas INT,
    precio           DECIMAL(10,2),
    observaciones    TEXT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (estado_evento_id) REFERENCES estado_evento(id)
);

-- 8. CONFIGURACIÓN
CREATE TABLE configuracion (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    clave       VARCHAR(50) NOT NULL UNIQUE,
    valor       VARCHAR(255) NOT NULL,
    descripcion TEXT
);


-- ============================================================
-- INSERCIÓN DE DATOS
-- ============================================================

-- Roles
INSERT INTO rol (nombre, descripcion) VALUES
('Administrador', 'Acceso total al sistema'),
('Recepcionista', 'Gestión de reservas y check-in/check-out'),
('Limpieza', 'Registro de limpieza de habitaciones'),
('Gerente', 'Supervisión general y reportes');

-- Usuarios
INSERT INTO usuario (nombre, apellido, cedula, email, password, rol_id) VALUES
('Carlos', 'Mendoza', 'V-12345678', 'carlos@hotel.com', SHA2('admin123', 256), 1),
('María', 'López', 'V-23456789', 'maria@hotel.com', SHA2('recep456', 256), 2),
('José', 'Ramírez', 'V-34567890', 'jose@hotel.com', SHA2('limp789', 256), 3),
('Ana', 'García', 'V-45678901', 'ana@hotel.com', SHA2('ger321', 256), 4);

-- Tipos de documento
INSERT INTO tipo_documento (nombre) VALUES
('Cédula de Identidad'),
('Pasaporte'),
('RIF'),
('Licencia de Conducir');

-- Clientes
INSERT INTO cliente (nombre, apellido, identificacion, telefono, email, nacionalidad, fecha_nacimiento, tipo_documento_id) VALUES
('Pedro', 'Martínez', 'V-11111111', '0412-1234567', 'pedro@gmail.com', 'Venezolano', '1990-05-15', 1),
('Laura', 'Fernández', 'E-22222222', '0414-7654321', 'laura@gmail.com', 'Colombiana', '1985-08-22', 2),
('Miguel', 'Torres', 'V-33333333', '0416-9876543', 'miguel@gmail.com', 'Venezolano', '1978-12-01', 1),
('Sofía', 'Rojas', 'V-44444444', '0424-1112233', NULL, 'Venezolana', '1995-03-10', 1),
('Ricardo', 'Díaz', 'E-55555555', '0412-4455667', 'ricardo@gmail.com', 'Ecuatoriano', NULL, 2);

-- Historial de clientes
INSERT INTO historial_cliente (cliente_id, usuario_id, observacion) VALUES
(1, 2, 'Cliente VIP, siempre solicita habitación en piso bajo'),
(2, 2, 'Alérgica al maní, informar a restaurante'),
(3, 1, 'Solicitó factura con datos fiscales especiales');

-- Tipos de unidad
INSERT INTO tipo_unidad (nombre) VALUES
('Individual'), ('Doble'), ('Suite'), ('Presidencial'), ('Familiar');

-- Estados de unidad
INSERT INTO estado_unidad (nombre) VALUES
('Disponible'), ('Ocupada'), ('Mantenimiento'), ('Limpieza');

-- Habitaciones
INSERT INTO habitacion (numero, piso, capacidad, descripcion, tipo_unidad_id, estado_unidad_id) VALUES
('101', 1, 1, 'Habitación individual con vista al jardín', 1, 1),
('102', 1, 2, 'Habitación doble estándar', 2, 1),
('201', 2, 2, 'Suite con jacuzzi', 3, 2),
('202', 2, 4, 'Habitación familiar amplia', 5, 1),
('301', 3, 2, 'Suite presidencial con terraza', 4, 3),
('302', 3, 1, 'Individual en piso superior', 1, 4);

-- Tarifas
INSERT INTO tarifa (temporadas, precio, fecha_inicio, fecha_fin, tipo_unidad_id) VALUES
('Temporada Baja', 50.00, '2026-01-01', '2026-03-31', 1),
('Temporada Baja', 80.00, '2026-01-01', '2026-03-31', 2),
('Temporada Alta', 120.00, '2026-07-01', '2026-09-30', 3),
('Temporada Alta', 250.00, '2026-07-01', '2026-09-30', 4),
('Temporada Media', 100.00, '2026-04-01', '2026-06-30', 5);

-- Estados de reserva
INSERT INTO estado_reserva (estado) VALUES
('Confirmada'), ('Pendiente'), ('Cancelada'), ('Completada');

-- Reservas
INSERT INTO reserva (cliente_id, habitacion_id, tarifa_id, estado_reserva_id, fecha_inicio, fecha_fin, cantidad, observaciones) VALUES
(1, 1, 1, 1, '2026-04-15', '2026-04-18', 1, 'Cliente frecuente, prefiere piso bajo'),
(2, 3, 3, 1, '2026-07-10', '2026-07-15', 2, 'Luna de miel'),
(3, 2, 2, 2, '2026-05-01', '2026-05-03', 2, NULL),
(4, 4, 5, 1, '2026-04-20', '2026-04-25', 4, 'Viaje familiar con niños'),
(5, 1, 1, 3, '2026-03-10', '2026-03-12', 1, 'Cancelada por el cliente');

-- Estadías
INSERT INTO estadia (reserva_id, usuario_checkin_id, usuario_checkout_id, fecha_checkin, fecha_checkout, estado) VALUES
(1, 2, 2, '2026-04-15 14:00:00', '2026-04-18 11:00:00', 'COMPLETADO'),
(2, 2, NULL, '2026-07-10 15:30:00', NULL, 'ACTIVO');

-- Limpieza
INSERT INTO limpieza (habitacion_id, usuario_id, estado, observacion) VALUES
(1, 3, 'Completada', 'Limpieza profunda realizada'),
(2, 3, 'Pendiente', 'Falta reponer amenities'),
(3, 3, 'Completada', NULL);

-- Facturas
INSERT INTO factura (cliente_id, reserva_id, descuento, total) VALUES
(1, 1, 10.00, 140.00),
(2, 2, 0.00, 600.00),
(4, 4, 25.00, 475.00);

-- Pagos
INSERT INTO pago (factura_id, usuario_id, monto, referencia_pago, tipo_pago, estado_pago) VALUES
(1, 2, 140.00, 'REF-001-2026', 'efectivo', 'completado'),
(2, 2, 300.00, 'REF-002-2026', 'digital', 'completado'),
(2, 2, 300.00, 'REF-003-2026', 'digital', 'pendiente'),
(3, 2, 475.00, NULL, 'efectivo', 'pendiente');

-- Tipos de servicio
INSERT INTO tipo_servicio (nombre) VALUES
('Restaurante'), ('Spa'), ('Lavandería'), ('Minibar'), ('Transporte');

-- Servicios
INSERT INTO servicio (nombre, tipo_servicio_id, precio_base) VALUES
('Desayuno Buffet', 1, 15.00),
('Masaje Relajante', 2, 45.00),
('Lavado y Planchado', 3, 10.00),
('Minibar Premium', 4, 25.00),
('Transfer Aeropuerto', 5, 35.00);

-- Consumo de servicios
INSERT INTO consumo_servicio (cliente_id, servicio_id, factura_id, cantidad, observacion) VALUES
(1, 1, 1, 3, 'Desayuno para 3 días'),
(1, 3, 1, 1, 'Lavado de traje'),
(2, 2, 2, 2, 'Masaje para pareja'),
(4, 1, 3, 5, 'Desayuno familiar 5 días');

-- Estados de evento
INSERT INTO estado_evento (nombre) VALUES
('Programado'), ('En Curso'), ('Finalizado'), ('Cancelado');

-- Eventos
INSERT INTO evento (nombre, cliente_id, estado_evento_id, tipo_evento, fecha, hora_inicio, hora_fin, cantidad_personas, precio, observaciones) VALUES
('Boda Martínez-López', 1, 1, 'Boda', '2026-06-15', '18:00:00', '23:00:00', 150, 5000.00, 'Decoración floral incluida'),
('Conferencia TechVzla', 3, 1, 'Conferencia', '2026-05-20', '09:00:00', '17:00:00', 80, 2000.00, NULL);

-- Configuración
INSERT INTO configuracion (clave, valor, descripcion) VALUES
('nombre_hotel', 'Hotel Gran Venezuela', 'Nombre comercial del hotel'),
('iva', '16', 'Porcentaje de IVA aplicable'),
('moneda', 'USD', 'Moneda principal de operación'),
('hora_checkout', '12:00', 'Hora límite de checkout'),
('max_reservas_dia', '50', 'Máximo de reservas por día');

-- Auditoría
INSERT INTO auditoria (usuario_id, accion, entidad, entidad_id, detalle, ip_address) VALUES
(1, 'INSERT', 'reserva', 1, 'Nueva reserva creada para Pedro Martínez', '192.168.1.10'),
(2, 'UPDATE', 'habitacion', 1, 'Estado cambiado a Ocupada', '192.168.1.15'),
(1, 'DELETE', 'reserva', 5, 'Reserva cancelada por solicitud del cliente', '192.168.1.10');


-- ============================================================
-- PROCEDIMIENTOS DE ACTUALIZACIÓN (UPDATE)
-- ============================================================

-- 1. Cambiar estado de habitación a "Ocupada" tras check-in
UPDATE habitacion SET estado_unidad_id = 2 WHERE id = 1;

-- 2. Registrar el checkout de una estadía
UPDATE estadia SET 
    fecha_checkout = NOW(), 
    usuario_checkout_id = 2, 
    estado = 'COMPLETADO' 
WHERE id = 2;

-- 3. Actualizar estado de pago a completado
UPDATE pago SET estado_pago = 'completado' WHERE id = 3;

-- 4. Desactivar un usuario que ya no trabaja en el hotel
UPDATE usuario SET activo = FALSE WHERE id = 3;

-- 5. Actualizar precio de una tarifa por inflación
UPDATE tarifa SET precio = 65.00 WHERE id = 1;


-- ============================================================
-- PROCEDIMIENTOS DE BORRADO (DELETE)
-- ============================================================

-- 1. Eliminar una reserva cancelada
DELETE FROM reserva WHERE id = 5 AND estado = 'ACTIVO';

-- 2. Eliminar un registro de limpieza incorrecto
DELETE FROM limpieza WHERE id = 2;

-- 3. Eliminar un tipo de servicio que ya no se ofrece
DELETE FROM tipo_servicio WHERE id = 5;

-- 4. Eliminar un evento cancelado
DELETE FROM evento WHERE id = 2 AND estado_evento_id = 4;

-- 5. Eliminar configuración obsoleta
DELETE FROM configuracion WHERE clave = 'max_reservas_dia';


-- ============================================================
-- 10 CONSULTAS SELECT CON OPERADORES AVANZADOS
-- ============================================================

-- CONSULTA 1: Buscar clientes cuyo nombre comience con "P" (LIKE)
SELECT * FROM cliente WHERE nombre LIKE 'P%';

-- CONSULTA 2: Buscar reservas en un rango de fechas (BETWEEN)
SELECT r.id, c.nombre, c.apellido, r.fecha_inicio, r.fecha_fin 
FROM reserva r 
JOIN cliente c ON r.cliente_id = c.id 
WHERE r.fecha_inicio BETWEEN '2026-04-01' AND '2026-04-30';

-- CONSULTA 3: Buscar habitaciones en estados específicos (IN)
SELECT h.numero, h.piso, eu.nombre AS estado 
FROM habitacion h 
JOIN estado_unidad eu ON h.estado_unidad_id = eu.id 
WHERE eu.nombre IN ('Disponible', 'Limpieza');

-- CONSULTA 4: Buscar clientes que NO tienen email registrado (IS NULL)
SELECT nombre, apellido, identificacion, telefono 
FROM cliente 
WHERE email IS NULL;

-- CONSULTA 5: Buscar servicios cuyo nombre contenga "Masaje" (LIKE)
SELECT s.nombre, ts.nombre AS categoria, s.precio_base 
FROM servicio s 
JOIN tipo_servicio ts ON s.tipo_servicio_id = ts.id 
WHERE s.nombre LIKE '%Masaje%';

-- CONSULTA 6: Buscar tarifas con precio entre $50 y $150 (BETWEEN)
SELECT t.temporadas, tu.nombre AS tipo_habitacion, t.precio 
FROM tarifa t 
JOIN tipo_unidad tu ON t.tipo_unidad_id = tu.id 
WHERE t.precio BETWEEN 50.00 AND 150.00;

-- CONSULTA 7: Buscar pagos con estado pendiente o cancelado (IN)
SELECT p.id, f.id AS factura, p.monto, p.tipo_pago, p.estado_pago 
FROM pago p 
JOIN factura f ON p.factura_id = f.id 
WHERE p.estado_pago IN ('pendiente', 'cancelado');

-- CONSULTA 8: Buscar estadías que aún no tienen checkout (IS NULL)
SELECT e.id, r.id AS reserva, c.nombre, c.apellido, e.fecha_checkin 
FROM estadia e 
JOIN reserva r ON e.reserva_id = r.id 
JOIN cliente c ON r.cliente_id = c.id 
WHERE e.fecha_checkout IS NULL;

-- CONSULTA 9: Buscar clientes colombianos o ecuatorianos con "a" en el nombre (IN + LIKE)
SELECT nombre, apellido, nacionalidad, email 
FROM cliente 
WHERE nacionalidad IN ('Colombiana', 'Ecuatoriano') 
AND nombre LIKE '%a%';

-- CONSULTA 10: Buscar eventos tecnológicos entre mayo y julio (BETWEEN + LIKE)
SELECT e.nombre, e.tipo_evento, e.fecha, e.cantidad_personas, e.precio, ee.nombre AS estado 
FROM evento e 
JOIN estado_evento ee ON e.estado_evento_id = ee.id 
WHERE e.fecha BETWEEN '2026-05-01' AND '2026-07-31' 
AND e.nombre LIKE '%Tech%';