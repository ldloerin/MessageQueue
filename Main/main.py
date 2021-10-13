import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.Output.write_dockerfile import WriteDockerfile


class BuildMailAddress(GetInput):
    def execute_workflow(self):
        self.__build_mail_adrress()
        self.__create_dockerfile()

    def __build_mail_adrress(self):
        self.mail_address = self.first_name
        self.mail_address += self.separator
        self.mail_address += self.last_name
        self.mail_address += "@"
        self.mail_address += self.domain
        self.mail_address = self.mail_address.lower()
        print(self.mail_address)

    def __create_dockerfile(self):
        self.root_path = (os.path.dirname(self.code_path))
        WriteDockerfile(self)


my_code = BuildMailAddress(__file__)
my_code.execute_workflow()
