import base64
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageGetter:

    def __init__(self) -> None:
        logger.info("ImageGetter initialized")

    con_parser_crz = {
        '01': 'apsp',
        '02': 'alsp',
        '03': 'aflp',
        '04': 'arbp',
        '05': 'afdp',
        '06': 'vptp'
    }

    @staticmethod
    def parse_link(id: str) -> dict:
        logger.info(f"Parsing link for ID: {id}")
        
        con = ImageGetter.con_parser_crz.get(id[:2])
        if id[2:4] == '51':
            praca = f'{id[2:4]}s'
        else:
            praca = id[2:4]

        options = {
            'opt1': f'https://imagens.arteris.com.br/Pictures/{id[9:17]}/{id[:9]}/{id}-L01.jpg',
            'opt2': f'https://{con}{praca}.arteris.com.br/Pictures/{id[9:17]}/{id[:9]}/{id}-L01.jpg'
        }

        logger.debug(f"Generated options: {options}")
        return options
    
    @staticmethod
    def encode_image(img):
        logger.info("Encoding image")
        try:
            encoded_image = base64.b64encode(img).decode('utf-8')
            logger.debug("Image encoded successfully")
        except Exception as e:
            logger.error("Failed to encode image", exc_info=e)
            raise e
        
        return encoded_image
    
    @staticmethod
    def get_image(links: dict):
        logger.info("Attempting to retrieve image from provided links")
        for url in links.values():
            try:
                logger.debug(f"Requesting image from URL: {url}")
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    logger.info(f"Image retrieved successfully from {url}")
                    return response.content
                else:
                    logger.warning(f"Received status code {response.status_code} for URL: {url}")
            except requests.RequestException as e:
                logger.error(f"Request failed for {url}: {e}")
        
        logger.error("No valid image could be retrieved from the provided links")
        return None
