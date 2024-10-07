from queue_setup.setup import Setup


def main():
    num_consumers = 5
    setup = Setup(num_consumers)
    
    print("Waiting for messages. To exit press CTRL+C")
    try:
        for channel in setup.channels:
            channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping consumers...")
        for channel in setup.channels:
            channel.stop_consuming()

if __name__ == '__main__':
    main()
