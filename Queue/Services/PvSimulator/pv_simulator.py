import os
import sys
parent_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(parent_path)
from Broker.consume import Consume
sys.path.append(os.path.dirname(__file__))
from generate_pv_curve import GeneratePvCurve
from calculate_total_power_curve import CalculateTotalPowerCurve
from create_output_text import CreateOutputText


class PvSimulator():
    def __init__(self, input):
        self.sunrize = input.sunrize
        self.sunset = input.sunset
        self.dawn = input.dawn
        self.max_pv_power = input.max_pv_power
        self.output_file = input.output_file
        self.time_points = input.time_points
        self.queue_name = input.queue_name
        self.__receive_data()
        self.__run_generate_pv_curve()
        self.__calculate_total_power_curve()
        self.__create_output_text()
        self.__write_output()

    def __receive_data(self):
        self.meter_curve = Consume(self).received_data

    def __run_generate_pv_curve(self):
        self.pv_curve = GeneratePvCurve(self).pv_curve

    def __calculate_total_power_curve(self):
        self.total_power_curve = CalculateTotalPowerCurve(self).total_power_curve

    def __create_output_text(self):
        self.output_text = CreateOutputText(self).output_text

    def __write_output(self):
        f = open(self.output_file, "w+")
        f.write(self.output_text)
        f.close()
