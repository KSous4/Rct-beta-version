from queue.connection import get_rabbit_manager
from handlers.message_handler import MsgHandler

class Setup:
    def __init__(self, num_consumers) -> None:
        self.rabbit_manager = get_rabbit_manager()
        self.channels = [self.rabbit_manager.create_channel() for _ in range(num_consumers)]
        self.queue_name = 'entrance_queue'
        self.setup_consumers()

    def setup_consumers(self):
        for channel in self.channels:
            channel.basic_consume(
                queue=self.queue_name,
                on_message_callback=self.callback,
                auto_ack=False
            )

    def callback(self, ch, method, properties, body):
        try:
            MsgHandler.classify(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing message: {e}")
