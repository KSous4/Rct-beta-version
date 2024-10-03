from fastapi import APIRouter, UploadFile, File
from app.services.requestService import ReqService

router = APIRouter()


@router.post('/classify')
async def classify(file: UploadFile = File(...)):
    return await ReqService.request_handler(file)

