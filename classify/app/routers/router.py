from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus
from app.routers.post import router as post

router = APIRouter()

@router.get("/health")
async def health_check():
    return JSONResponse(status_code=HTTPStatus.OK,content={'status':'healthy'})

router.include_router(post)