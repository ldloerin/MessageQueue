import pika


class Publish:
    def send_message(current_time_point, queue_name):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange="", routing_key=queue_name, body=current_time_point)
        # print('Transferred: ' + current_time_point)
        connection.close()
