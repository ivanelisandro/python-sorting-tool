from processors import ProcessorOutputs, ProcessorTypes, ProcessorFactory
import sys


class ArgumentParser:
    datatype_option = "-dataType"
    sort_integers_option = "-sortIntegers"

    def __init__(self):
        self.datatype = ProcessorTypes.word
        self.output_option = ProcessorOutputs.summary
        self.arguments = sys.argv[1:] if len(sys.argv) > 1 else None

    def process(self):
        if not self.arguments:
            return

        for index, argument in enumerate(self.arguments):
            if argument == self.sort_integers_option:
                self.output_option = ProcessorOutputs.sorted_items
                self.datatype = ProcessorTypes.integer
                return
            if argument == self.datatype_option and len(self.arguments) > 1:
                self.datatype = self.arguments[index + 1]


parser = ArgumentParser()
parser.process()

factory = ProcessorFactory()
processor = factory.create(parser.datatype)

while True:
    try:
        data = input()
        processor.process(data)
    except EOFError:
        break

processor.print(parser.output_option)
