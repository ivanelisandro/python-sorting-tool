from arguments import ArgumentParser
from processors import ProcessorFactory


parser = ArgumentParser()
parser.process()

datatype, output = parser.get_options_values()
if not datatype or not output:
    exit()

factory = ProcessorFactory()
processor = factory.create(datatype)

while True:
    try:
        data = input()
        processor.process(data)
    except EOFError:
        break

processor.print(output)
