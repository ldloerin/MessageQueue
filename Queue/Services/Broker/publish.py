import pika


class Publish():
    def __init__(self, input):
        self.my_data = input.current_time_point
        self.queue_name = input.queue_name
        self.__send_message()

    def __send_message(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_publish(exchange="", routing_key=self.queue_name, body=self.my_data)
        # print('Transferred: ' + self.my_data)
        connection.close()
