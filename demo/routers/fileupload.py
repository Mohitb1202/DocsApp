from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..import models,schemas
from typing import List
from fastapi import HTTPException,File,UploadFile
from fastapi import status,Response


router=APIRouter(
    tags=['files']
)

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}