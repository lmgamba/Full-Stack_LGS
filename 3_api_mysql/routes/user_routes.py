from fastapi import APIRouter, Depends, Path
from controllers import user_controller
from models.user_model import *
from core.dependencies import get_current_user, is_admin_or_owner

# solo importamos APIRouter porque este fichero ya nos encontramos en la ruta /users, aqui tengo que montar todas las subrutas a partir de ese elemento.

router = APIRouter()

# obtener usuario por id http://localhost:8000/users/


##########VERSION CON AUTENTIFICACION#############
## Se pone user=Depends(get_current_user) como otro parametro  para que se ejecute la dependencia y compruebe el token
@router.get('/{user_id}', status_code= 200)
async def get_users_by_id(user_id: str, user=Depends(is_admin_or_owner)):
     return await user_controller.obtener_usuario_by_id(int(user_id))
##  -> de esta forma no deja leer el id sin que "seamos " el usuario logeado
# en peticiones. rest se añade:
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUsInJvbCI6InVzZXIiLCJleHBpcmUiOjE3NjgwNzE1MDd9.YqyO7wYH1uU5xQD03Lee5_dCk5WPE4LHdT-B6h21_9g



"""
VERSION SIN AUTENTIFICACION

@router.get('/{user_id}', status_code= 200)
async def get_users_by_id(user_id: str):
    #llama al controlador a la funcion obtener_usuarios por id -->>> RECORDAR pasar id a int
    return await user_controller.obtener_usuario_by_id(int(user_id))
    """

# obtener usuario por edades http://localhost:8000/users/

"""
FILTRO EDAD OPCION 2: USANDO queryparams
con queryparams la ruta seria como:

http://localhost:8000/users/filter/age?agemin=12&agemax=24&name="juan"

esta ruta esta asignando los parametros:
agemin = 12 de tipo int => NO HAY QUE PASARLO A INT DENTRO DE LA FUNCION
agemax =24 de tipo int
name = juan, de tipo string (por eso con comillas)

@router.get('/filter/edad', status_code= 200)
def get_users_by_age(agemin: int,agemax: int):
    return  user_controller.obtener_usuarios_by_age(int(agemin),int(agemax))
"""

@router.get('/filter/edad', status_code= 200)
async def get_users_by_age(agemin: int,agemax: int):
    return await user_controller.obtener_usuarios_by_age(agemin,agemax)

@router.post('/register', status_code= 201)
async def register(user: UserCreate):
    return await user_controller.registrar(user)

@router.delete('/{user_id}', status_code= 200)
async def delete_user_by_id(user_id: str):
    return await user_controller.borrar_usuario_by_id(int(user_id))


# update  con PUT
@router.put('/{user_id}', status_code= 200)
async def update_user_by_id(user_id: str, user: User):
    return await user_controller.actualizar_usuario_by_id(int(user_id), user)