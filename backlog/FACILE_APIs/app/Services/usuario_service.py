from app.Data.usuarios_db import usuarios

def listar_usuarios():
    return usuarios


def obtener_usuario(id_usuario: int):

    for usuario in usuarios:

        if usuario["id"] == id_usuario:
            return usuario

    return None


def crear_usuario(usuario):

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "cedula": usuario.cedula,
        "correo": usuario.correo,
        "rol": usuario.rol,
        "activo": True
    }

    usuarios.append(nuevo_usuario)

    return nuevo_usuario