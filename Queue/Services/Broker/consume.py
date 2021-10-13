import pika


class Consume():
    def __init__(self, input):
        self.time_points = input.time_points
        self.queue_name = input.queue_name
        self.received_data = []
        self.__receive_message()

    def __receive_message(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.__callback)
        self.channel.start_consuming()

    def __callback(self, ch, method, properties, body):
        print("Received %r" % body)
        self.__store_message(body)  

    def __store_message(self, body):
        current_data = body.decode("utf-8")
        current_data = current_data.replace('[', '')
        current_data = current_data.replace(']', '')
        current_data = current_data.replace(' ', '')
        current_data = current_data.replace('"', '')
        current_data = current_data.replace("'", '')
        current_data = current_data.split(',')
        time = current_data[0]
        value = float(current_data[1])
        self.received_data.append([time, value])
        if len(self.received_data) == len(self.time_points):
            self.channel.stop_consuming()
