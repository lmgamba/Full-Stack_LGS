from fastapi import HTTPException, Depends, Path
from fastapi.security import OAuth2PasswordBearer
from controllers.user_controller import obtener_usuario_by_id
from core.security import decode_token

oauth2= OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token:str= Depends(oauth2)):
    #decodificar token
    payload = decode_token(token)
    print(payload)
    if not payload :
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecto")
    user_id= payload.get('id')
    if not user_id:
        raise HTTPException(status_code= 404, detail="Usuario o contraseña incorrecto")
    
    usuario= await obtener_usuario_by_id(user_id)
    return usuario

async def is_admin_or_owner(user=Depends(get_current_user), user_id: int =Path(...)):
    #comprobar si el usuario es admin
    if user['rol'] == 'admin':
        return user 
    #comprobar si el usuario es el propietario
    if user['id'] == user_id:
        return user
    
    raise HTTPException(status_code=403, detail="No tienes permisos para realizar esta accion")

    
    