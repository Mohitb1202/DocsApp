from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models,schemas
from passlib.context import CryptContext

router=APIRouter(
    tags=['user']
)


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

@router.post('/user',response_model=schemas.DisplayUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_user=models.User(username=request.username,email=request.email,password=hashedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user