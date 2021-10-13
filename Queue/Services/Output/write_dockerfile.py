import codecs
import os


class WriteDockerfile:
    def execute_workflow(self,dockerfile, output_content):
        self.__build_content(output_content)
        self.__write_file(dockerfile)

    def __build_content(self, output_content):
        output_content = output_content.replace("\n\n", ",")
        output_content = output_content.replace("\n", ",")
        output_content = output_content.split(",")
        self.docker_content = "FROM ubuntu\n\n"
        self.docker_content += "RUN apt-get update\n\n"
        for line in output_content:
            self.docker_content += 'CMD ["echo", "' + line + '"]\n\n'

    def __write_file(self, dockerfile):
        f = codecs.open(dockerfile, "w", "utf-8")
        f.write(self.docker_content)
        f.close()
