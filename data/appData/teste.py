import pika
import os
import pika.credentials


rabbit_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbit_user = os.getenv('RABBITMQ_USER', 'guest')
rabbit_pass = os.getenv('RABBITMQ_PASS', 'guest')


credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)

# Establish connection parameters
parameters = pika.ConnectionParameters(host=rabbit_host, credentials=credentials)


connection = pika.BlockingConnection(parameters)
print("Connected to RabbitMQ")

# Create a channel
channel = connection.channel()

channel.queue_delete("Review Transit")

