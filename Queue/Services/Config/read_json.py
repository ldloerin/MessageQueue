import json
import os
import sys


class ReadJson:
    def read_json_file(json_file):
        if os.path.isfile(json_file):
            try:
                with open(json_file, encoding="utf-8") as encoded_json_file:
                    inputs = json.load(encoded_json_file)
                    return inputs
            except Exception as e:
                warning_message = "\n\nWarning: Could not read " + json_file + "\n"
                warning_message += str(e) + "\n\n"
                sys.exit(warning_message)
        else:
            warning_message = "\n\nWarning: Could not find " + json_file + "\n\n"
            sys.exit(warning_message)
