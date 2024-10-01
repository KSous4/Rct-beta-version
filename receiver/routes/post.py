from fastapi import APIRouter, Request , Depends
from receiver.services.enqueue import EnqueueService
from receiver.queue.connection import RabbitManager,get_rabbit_manager

router = APIRouter()


@router.post("/validate")
async def validate(
    request: Request,
    rabbit_manager: RabbitManager = Depends(get_rabbit_manager)
):
    return await EnqueueService.enqueue(request, rabbit_manager)

@router.post("/enqueue")
async def validate(
    request: Request,
    rabbit_manager: RabbitManager = Depends(get_rabbit_manager)
):
    return await EnqueueService.enqueue_any(request, rabbit_manager)


