from json import dumps, loads, JSONDecodeError
from utils.image_getter import ImageGetter
from requests import post
class MsgHandler:

    def __init__() -> None:
        pass

    def classify(rabbit_conn,channel,body):
    
        try:
            msg = loads(body.decode('utf-8'))
            
            id = msg.get('id')

            data = ImageGetter.parse_link(id)


            try :
                post('https:///classifier/classify')
            except:
                raise

            files = [(
                'file',
                (
                    open('./image.jpg')
                )
            )]


            rabbit_conn.publish_message(
                'exit_queue',channel,dumps(data)
            )





        except (JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error processing message: {e}")
