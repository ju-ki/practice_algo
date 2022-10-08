import os

class InputCount:
    input_count = -1


class OutputCount:
    output_count = -1


class TestRunner():
    def __init__(self, path, fileName, project="algo"):
        self.path = path
        self.fileName = fileName
        if project == "test":
            self.input_path = self.path + "/" + self.fileName + "/input.txt"
            self.output_path = self.path + "/" + self.fileName + "/output.txt"
        else:
            self.input_path = self.path + "/" + project + "/"  + self.fileName + "/input.txt"
            self.output_path = self.path + "/" + project + "/" + self.fileName + "/output.txt"

    def input(self):
        with open(self.input_path, "r") as f:
            lines = f.read()
            InputCount.input_count += 1
            return lines.split("\n")[InputCount.input_count]

    def answer(self, output):
        RED = '\033[31m'
        END = '\033[0m'
        GREEN = '\033[32m'
        with open(self.output_path, "r") as f:
            lines = f.read()
            OutputCount.output_count += 1
            if type(output) == int:
                _answer = int(lines.split("\n")[OutputCount.output_count])
            elif type(output) == str:
                _answer = lines.split("\n")[OutputCount.output_count]
            if output == _answer:
                print(GREEN + "AC" + END)
                print(GREEN + "answer:" + str(_answer) + END)
            elif output != _answer:
                print(RED + "WA" + END)
                print(RED + "answer:" + str(_answer) + END)
