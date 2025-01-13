from processors import ProcessorOutputs, ProcessorTypes, ProcessorFactory
import sys


class ArgumentParser:
    datatype_option = "-dataType"
    sorting_option = "-sortingType"

    def __init__(self):
        self.arguments = sys.argv[1:] if len(sys.argv) > 1 else None
        self.options = {
            self.datatype_option : ProcessorTypes.word,
            self.sorting_option : ProcessorOutputs.sorted,
        }

    def process(self):
        if not self.arguments:
            return

        for index, argument in enumerate(self.arguments):
            if argument in self.options:
                self.set_option(index, argument)

    def set_option(self, current_index, option):
        option_value_index = current_index + 1
        if option_value_index < len(self.arguments):
            self.options[option] = self.arguments[option_value_index]

    def get_datatype(self):
        return self.options[self.datatype_option]

    def get_output(self):
        return self.options[self.sorting_option]


parser = ArgumentParser()
parser.process()

factory = ProcessorFactory()
processor = factory.create(parser.get_datatype())

while True:
    try:
        data = input()
        processor.process(data)
    except EOFError:
        break

processor.print(parser.get_output())
