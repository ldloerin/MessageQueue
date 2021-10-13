import multiprocessing
import os
import random
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Meter.meter import Meter
from Services.Output.write_dockerfile import WriteDockerfile
from Services.PvSimulator.pv_simulator import PvSimulator


class ControlQueue(GetInput):
    def execute_workflow(self, my_rand):
        parent_dir = os.path.dirname(__file__)
        self.measure_time_points = os.path.join(parent_dir, 'Input', 'measure_time_points.csv')
        self.output_file = os.path.join(os.path.dirname(parent_dir), 'Output', 'results.csv')
        self.queue_name = self.queue_name + '_' + str(my_rand)
        self.__read_measure_time_points()

    def __read_measure_time_points(self):
        f = open(self.measure_time_points, "r")
        self.time_points = f.readlines()[1:]
        f.close()

    def __create_dockerfile(self):
        root_path = (os.path.dirname(self.code_path))
        WriteDockerfile(root_path, self.output_content)

    def run_meter_process(self):
        Meter(self)

    def run_pv_simulator_process(self):
        pv_simulator = PvSimulator(self)
        self.output_content = pv_simulator.output_text
        print(self.output_content)
        self.__create_dockerfile()


my_rand = random.randrange(0, 1e9)
my_queue = ControlQueue(__file__)
my_queue.execute_workflow(my_rand)
p1 = multiprocessing.Process(target=my_queue.run_meter_process)
p2 = multiprocessing.Process(target=my_queue.run_pv_simulator_process)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
