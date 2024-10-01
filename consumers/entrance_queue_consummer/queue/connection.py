import pika
import os

class RabbitManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if RabbitManager._instance is not None:
            raise Exception("Cannot instantiate RabbitManager: This class is a singleton.")
        self.connection = self.create_connection()
        
    def create_connection(self):
        rabbit_host = os.getenv('RABBITMQ_HOST', 'localhost')
        rabbit_user = os.getenv('RABBITMQ_USER', 'guest')
        rabbit_pass = os.getenv('RABBITMQ_PASS', 'guest')

        credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
        parameters = pika.ConnectionParameters(
            host=rabbit_host,
            credentials=credentials,
            heartbeat=0,
            virtual_host='rabbitmq'
        )
        
        connection = pika.BlockingConnection(parameters)
        return connection

    def create_channel(self):
        self.ensure_connection()
        return self.connection.channel()
    
    def close_channel(self, channel):
        if channel.is_open:
            channel.close()
        else:
            print("Channel is already closed.")

    def ensure_connection(self):
        if self.connection.is_open:
            return
        self.connection = self.create_connection()
    
    def publish_message(self,queue_name, channel, message):
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        self.close_channel(channel)

def get_rabbit_manager():
    return RabbitManager.get_instance()
