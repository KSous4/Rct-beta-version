import json
class MsgHandler:

    def __init__(self) -> None:
        pass

    def classify(body):
    
        try:
            msg = json.loads(body.decode('utf-8'))
            
            print(msg.keys())

            return 0
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error processing message: {e}")
            return -1
