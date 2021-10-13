import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from Main.main import BuildMailAddress


class RunBuildMailAddress():
    def __init__(self, input):
        parent_path = os.path.split(os.path.dirname(__file__))[0]
        self.test_code_file = os.path.join(
            os.path.dirname(parent_path),
            input.test_code_path,
            input.test_code_name,
        )
        self.__execute_workflow()

    def __execute_workflow(self):
        my_code = BuildMailAddress(self.test_code_file)
        my_code.execute_workflow()
        self.mail_address = my_code.mail_address
