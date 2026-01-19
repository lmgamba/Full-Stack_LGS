from fastapi import APIRouter
from models.user_model import *
from controllers import auth_controller
from core.security import *

router= APIRouter()

#registro de usuarios
#insercion de user a base de datos auth/register

@router.post('/register', status_code= 201)
async def register(user: UserCreate):
    return await auth_controller.registrar(user)

@router.post('/login', status_code= 200)
async def login(user_login: UserLogin):
    return await auth_controller.login(user_login)