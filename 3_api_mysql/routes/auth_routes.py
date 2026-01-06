from fastapi import APIRouter
from models.user_model import UserCreate
from controllers import auth_controller

router= APIRouter()

#registro de usuarios
#insercion de user a base de datos auth/register

@router.post('/register', status_code= 201)
async def register(user: UserCreate):
    return await auth_controller.registrar(user)