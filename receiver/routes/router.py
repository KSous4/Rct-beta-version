from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus
from receiver.routes.post import router as post_router

router = APIRouter()

@router.get("/health")
async def health_check():
    return JSONResponse(status_code=HTTPStatus.OK,content={'status':'healthy'})

router.include_router(post_router)
