import os
from Services.Config.read_json_file import ReadJsonFile


class GetInput:
    def __init__(self, main_code_file):
        self.code_path = os.path.dirname(main_code_file)
        self.__get_input_parameters()

    def __get_input_parameters(self):
        parameter_file = os.path.join(self.code_path, "Input", "config.json")
        parameter_file = parameter_file.replace("\\", "/")
        inputs = ReadJsonFile.load(parameter_file)
        for key, value in inputs.items():
            setattr(self, key, value)
