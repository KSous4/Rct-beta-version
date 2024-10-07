import logging
from json import dumps, loads, JSONDecodeError
from utils.image_getter import ImageGetter
from utils.config import Configs
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MsgHandler:

    def __init__(self) -> None:        
        logger.info("MsgHandler initialized")

    API_CONFIG = Configs.get_api_configs('../config/config.toml')
    API_KEY = API_CONFIG.get('API_KEY')
    API_URL = API_CONFIG.get('API_URL')

    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': ('Bearer ' + API_KEY)
    }

    @staticmethod
    def classify(rabbit_conn, channel, body):
        logger.info("Received message from RabbitMQ")
        
        try:
            msg = loads(body.decode('utf-8'))
            logger.debug(f"Decoded message: {msg}")
        except JSONDecodeError as e:
            logger.error("Failed to decode message", exc_info=e)
            return
        
        id = msg.get('id')
        logger.info(f"Processing image with ID: {id}")

        data = ImageGetter.parse_link(id)
        logger.debug(f"Parsed link: {data}")

        img = ImageGetter.get_image(data)
        logger.debug("Image retrieved")

        encoded_image = ImageGetter.encode_image(img)
        logger.debug("Image encoded")

        send_data = {
            'data':encoded_image
        }

        try:
            classification_response = requests.post(
                url=MsgHandler.API_URL,
                headers=MsgHandler.HEADERS,
                data= str.encode(dumps(send_data)),verify=False
            )
            classification_response.raise_for_status()
            classification = classification_response.json()
            logger.info("Classification successful")
        except requests.exceptions.RequestException as e:
            logger.error("Request to classification API failed", exc_info=e)
            return

        logger.debug(f"Classification result: {classification}")
        rabbit_conn.publish_message('exit_queue', channel, dumps(classification))
        logger.info("Published classification to exit_queue")
