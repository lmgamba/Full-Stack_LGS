from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    mail:str
    register: Optional[datetime]=None
    status:int
    password:str
    rol:str
    
class UserCreate(BaseModel):
    name:str
    surname:str
    age:int
    mail:str
    register: Optional[datetime]=None
    status:int
    password:str
    rol:str
    
class UserLogin(BaseModel):
    mail:str
    password:str