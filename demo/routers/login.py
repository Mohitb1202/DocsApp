from fastapi import APIRouter,Depends,status,HTTPException
from ..import schemas,database,models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..schemas import TokenData

SECRET_KEY="e217odcnjd9o2sn1289129120qwxa327asjk3923e3nnd"
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=20

router=APIRouter()


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def generate_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    seller=db.query(models.User).filter(models.User.username==request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='invalid user')
    if not pwd_context.verify(request.password,seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')

    #Gen JWT Token
    access_token=generate_token(
        data={'sub':seller.username}
    )
    return {"access_token":access_token,"token_type":"bearer"}

def get_current_user(token:str=Depends(oauth2_scheme)):
    credential_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid auth credentials",
        headers={'WWW-authenticate':"Bearer"},
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        if username is None:
            raise credential_exception
        token_data=TokenData(username=username)

    except JWTError:
        raise credential_exception