import os
import random
import sys
parent_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(parent_path)
from Broker.publish import Publish


class Meter():
    def __init__(self, input):
        self.time_points = input.time_points
        self.queue_name = input.queue_name
        self.__iterate_time_points()

    def __iterate_time_points(self):
        for time in self.time_points:
            self.time = time.replace('\n', '')
            self.__calc_random_power_values()
            self.__send_data()

    def __calc_random_power_values(self):
        random_power = random.randrange(0, 9000) / 1000
        self.current_time_point = str([self.time, random_power])

    def __send_data(self):
        Publish(self)
