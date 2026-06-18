from fastapi import APIRouter

from app.Schemas.usuario_schema import UsuarioCreate
from app.Services.usuario_service import (
    listar_usuarios,
    obtener_usuario,
    crear_usuario
)

router = APIRouter()

@router.get("/")
def get_usuarios():
    return listar_usuarios()


@router.get("/{id_usuario}")
def get_usuario(id_usuario: int):

    usuario = obtener_usuario(id_usuario)

    if usuario:
        return usuario

    return {"mensaje": "Usuario no encontrado"}


@router.post("/")
def post_usuario(usuario: UsuarioCreate):
    return crear_usuario(usuario)