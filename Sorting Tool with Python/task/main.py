from arguments import ArgumentParser
from processors import ProcessorFactory


parser = ArgumentParser()
parser.process()

datatype, output, input_path, output_path = parser.get_options_values()
if not datatype or not output:
    exit()

factory = ProcessorFactory()
processor = factory.create(datatype, output, input_path, output_path)

if processor:
    processor.load_data()
    processor.write_data()
