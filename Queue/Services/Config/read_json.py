import json
import os
import sys


class ReadJson:
    def read_json_file(json_file):
        if os.path.isfile(json_file):
            try:
                with open(json_file, encoding = "utf-8") as encoded_json_file:
                    inputs = json.load(encoded_json_file)
                    return inputs
            except:
                warning_message = "Warning: Could not read " + json_file
                sys.exit(warning_message)
        else:
            warning_message = "Warning: Could not find " + json_file
            sys.exit(warning_message)
