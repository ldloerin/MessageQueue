import os
import random
import sys
parent_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(parent_path)
from Broker.publish import Publish


class Meter:
    def iterate_time_points(self, time_points, queue_name):
        for time in time_points:
            self.time = time.replace('\n', '')
            self.__calc_random_power_values()
            self.__send_data(queue_name)

    def __calc_random_power_values(self):
        random_power = random.randrange(0, 9000) / 1000
        self.current_time_point = str([self.time, random_power])

    def __send_data(self, queue_name):
        my_publish = Publish.send_message(self.current_time_point, queue_name)
