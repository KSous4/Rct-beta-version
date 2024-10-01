from fastapi import Request, HTTPException
from http import HTTPStatus
from xmltodict import parse as xml_to_dict
from pydantic import ValidationError
from json import loads, dumps
from pika.exceptions import AMQPConnectionError
from receiver.queue.connection import RabbitManager
from receiver.models.ReviewTransitModel import Ns2ReviewTransit
from receiver.utils.files_handler import Filemanager

class EnqueueService:

    def __init__(self) -> None:
        pass

    @staticmethod
    async def enqueue(
        request: Request,
        rabbit_manager: RabbitManager
    ):
        rabbit_manager.ensure_connection()

        if request.headers.get('content-type') != 'text/xml':
            raise HTTPException(status_code=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

        body = await request.body()

        try:
            body = xml_to_dict(body)['soap:Envelope']['soap:Body']['ns2:ReviewTransit']
        except Exception as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, 
                detail=str(e))

        try:
            Ns2ReviewTransit.model_validate(body)
        except ValidationError as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST, 
                detail=loads(e.json()))

        data: dict = Filemanager.get_data_to_inference(body)

        try:
            channel = rabbit_manager.create_channel()
            rabbit_manager.publish_message('entrance_queue',channel,dumps(data))
            
            
        except AMQPConnectionError:
            raise HTTPException(
                status_code=HTTPStatus.SERVICE_UNAVAILABLE, 
                detail="RabbitMQ closed the connection")
        

    async def enqueue_any(
        request: Request,
        rabbit_manager: RabbitManager
    ):

        rabbit_manager.ensure_connection()

        body = await request.json()

        print(body)

        try:
            channel = rabbit_manager.create_channel()
            rabbit_manager.publish_message('entrance_queue',channel,dumps(body)) 
        except TypeError as e:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e)) 
        except AMQPConnectionError:
            raise HTTPException(
                status_code=HTTPStatus.SERVICE_UNAVAILABLE, 
                detail="RabbitMQ closed the connection")