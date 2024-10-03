from fastapi import FastAPI
from app.routers.router import router



app = FastAPI(
    title='classifier module'
)

app.include_router(router)