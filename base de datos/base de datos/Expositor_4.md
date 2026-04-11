# EXPOSITOR 4 — Procedimientos de Actualización (UPDATE) y Borrado (DELETE)

---

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
