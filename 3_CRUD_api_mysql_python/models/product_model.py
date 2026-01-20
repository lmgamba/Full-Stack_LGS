from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class product(BaseModel):
    id:int
    title:str
    price:float
    quantity:int
    status:int
    
class productCreate(BaseModel):
    title:str
    price:float
    quantity:int
    status:int