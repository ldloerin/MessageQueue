import codecs
import os


class WriteDockerfile():
    def __init__(self, root_path, output_content):
        self.dockerfile = os.path.join(root_path, 'Docker', 'dockerfile')
        self.output_content = output_content
        self.__build_content()
        self.__write_file()

    def __build_content(self):
        self.output_content = self.output_content.replace("\n\n", ",")
        self.output_content = self.output_content.replace("\n", ",")
        self.output_content = self.output_content.split(",")
        self.docker_content = "FROM ubuntu\n\n"
        self.docker_content += "RUN apt-get update\n\n"
        for line in self.output_content:
            self.docker_content += 'CMD ["echo", "' + line + '"]\n\n'

    def __write_file(self):
        f = codecs.open(self.dockerfile, "w", "utf-8")
        f.write(self.docker_content)
        f.close()
