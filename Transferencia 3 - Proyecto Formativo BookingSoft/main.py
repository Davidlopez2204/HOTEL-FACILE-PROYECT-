from fastapi import FastAPI
from database import Base, engine
from middleware.cors import configurar_cors

from routes import roles, usuarios, clientes, habitaciones, reservas, facturas, pagos, servicios, eventos

# Crear tablas al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
configurar_cors(app)

# Registrar rutas
app.include_router(roles.router)
app.include_router(usuarios.router)
app.include_router(clientes.router)
app.include_router(habitaciones.router)
app.include_router(reservas.router)
app.include_router(facturas.router)
app.include_router(pagos.router)
app.include_router(servicios.router)
app.include_router(eventos.router)
