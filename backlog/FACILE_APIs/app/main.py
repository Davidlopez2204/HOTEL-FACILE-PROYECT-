from fastapi import FastAPI

from app.Api.usuarios import router as usuarios_router

app = FastAPI(
    title="FACILE PMS",
    version="1.0.0"
)

app.include_router(
    usuarios_router,
    prefix="/api/v1/usuarios",
    tags=["Usuarios"]
)

@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a FACILE PMS"
    }