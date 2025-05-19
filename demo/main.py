from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users,login,fileupload


app=FastAPI()



app.include_router(users.router)
app.include_router(login.router)
app.include_router(fileupload.router)
models.Base.metadata.create_all(engine)






