import os
from TestServices.Config.read_test_json_file import ReadTestJsonFile


class GetTestInput:
    def __init__(self, main_code_file):
        self.code_path = os.path.dirname(main_code_file)
        self.root_path = os.path.dirname(self.code_path)
        self.__get_input_parameters()

    def __get_input_parameters(self):
        parameter_file = os.path.join(self.code_path, "Input", "config.json")
        parameter_file = parameter_file.replace("\\", "/")
        inputs = ReadTestJsonFile.load(parameter_file)
        for key, value in inputs.items():
            setattr(self, key, value)
