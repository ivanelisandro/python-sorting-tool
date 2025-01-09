from processors import ProcessorFactory
import sys

class ArgumentParser:
    datatype_pattern = "-dataType"

    def __init__(self):
        self.datatype = "word"
        self.arguments = sys.argv[1:] if len(sys.argv) > 2 else None

    def process(self):
        if not self.arguments:
            return

        for index, argument in enumerate(self.arguments):
            if argument == self.datatype_pattern:
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

processor.print_summary()
