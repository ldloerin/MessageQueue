import time
import multiprocessing
import random
import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Meter.meter import Meter
from Services.PvSimulator.pv_simulator import PvSimulator
from Services.Output.write_dockerfile import WriteDockerfile


class ControlQueue(GetInput):
    def execute_workflow(self):
        print(self.queue_name)
        self.__create_dockerfile()

    def __create_dockerfile(self):
        output_content = "Message Queue"
        root_path = (os.path.dirname(self.code_path))
        WriteDockerfile(root_path, output_content)


my_code = ControlQueue(__file__)
my_code.execute_workflow()
