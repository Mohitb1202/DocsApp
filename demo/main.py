from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users,login,fileupload


app=FastAPI(
    title="Products API",
    description="Get details for all the products on our website",
    terms_of_service="http://www.google.com",
    contact={
        "Developer Name":"Demo patel",
        "website":"http://www.google.com",
        "email":"demo@gmail.com"
    },
    license_info={
        "name":"XYZ",
        "url":"http://www.google.com"
    },
    #docs_url="/documentation",redoc_url=None
)



app.include_router(users.router)
app.include_router(login.router)
app.include_router(fileupload.router)
models.Base.metadata.create_all(engine)






