from receiver.queue.setup import Setup
from receiver.routes.router import router
from fastapi import FastAPI
import os


app = FastAPI(
    title="Receiver",
    description="Receive a CM request and put in queue to classify",
    version='1.1'
)

Setup.start_queues()

app.include_router(router)