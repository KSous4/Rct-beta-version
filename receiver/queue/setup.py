from receiver.queue.connection import get_rabbit_manager


class Setup:

    def __init__(self) -> None:
        pass
    def start_queues():
        rabbit_manager = get_rabbit_manager()

        channel = rabbit_manager.create_channel()

        queue_names = ['entrance_queue','exit_queue']
        for q in queue_names:
            channel.queue_declare(queue=q,durable=False)