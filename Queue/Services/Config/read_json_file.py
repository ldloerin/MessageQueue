import json
import os


class ReadJsonFile:
    def is_json_path_valid(json_path):
        is_valid = os.path.exists(json_path)
        is_valid &= os.path.isfile(json_path)
        return is_valid

    def load(json_path):
        if ReadJsonFile.is_json_path_valid(json_path):
            with open(json_path, "r") as json_path:
                inputs = json.load(json_path)
                return inputs
