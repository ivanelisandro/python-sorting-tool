from abc import ABC, abstractmethod


class ProcessorOutputs:
    """
    Defines the types of outputs available.
    """
    summary = "summary"
    sorted_items = "sorted"


class Processor(ABC):
    """
    Abstract class for processing some type of data.
    """
    def __init__(self):
        self.outputs = {}

    @abstractmethod
    def process(self, current_input):
        """
        Abstract method, must be implemented in child class.
        """
        pass

    def print(self, output_type:str):
        """
        Prints the output according to the type required by the application.
        :param output_type: Must be one of the ProcessorOutputs.
        """
        if output_type in self.outputs:
            self.outputs[output_type]()

class IntegerProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.numbers = []
        self.outputs[ProcessorOutputs.summary] = self.print_summary
        self.outputs[ProcessorOutputs.sorted_items] = self.print_sorted

    def process(self, current_input):
        items = current_input.split()
        for item in items:
            self.numbers.append(int(item))

    def print_summary(self):
        total = len(self.numbers)
        greatest = max(self.numbers)
        greatest_count = self.numbers.count(greatest)
        rate = int(greatest_count * 100 / total)

        print(f"Total numbers: {total}.")
        print(f"The greatest number: {greatest} ({greatest_count} time(s), {rate}%).")

    def print_sorted(self):
        self.numbers.sort()
        total = len(self.numbers)
        sorted_numbers = " ".join(str(number) for number in self.numbers)
        print(f"Total numbers: {total}.")
        print(f"Sorted data: {sorted_numbers}")


class StringProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.contents = []

    def process(self, current_input):
        pass

    def calculate_statistics(self):
        total = len(self.contents)
        longest = max([len(content) for content in self.contents])
        longest_elements = [content for content in self.contents if len(content) == longest]
        longest_count = len(longest_elements)
        rate = int(longest_count * 100 / total)
        return total, longest, longest_elements, longest_count, rate


class LineProcessor(StringProcessor):
    def __init__(self):
        super().__init__()
        self.outputs[ProcessorOutputs.summary] = self.print_summary

    def process(self, current_input):
        self.contents.append(current_input)

    def print_summary(self):
        (total, longest, elements, longest_count, rate) = self.calculate_statistics()

        elements.sort()
        print(f"Total lines: {total}.")
        print(f"The longest line:")
        print(*elements, sep='\n')
        print(f"({longest_count} time(s), {rate}%).")


class WordProcessor(StringProcessor):
    def __init__(self):
        super().__init__()
        self.outputs[ProcessorOutputs.summary] = self.print_summary

    def process(self, current_input):
        items = current_input.split()
        for item in items:
            self.contents.append(item)

    def print_summary(self):
        (total, longest, elements, longest_count, rate) = self.calculate_statistics()

        elements.sort()
        print(f"Total words: {total}.")
        print(f"The longest word: {" ".join(elements)} ({longest_count} time(s), {rate}%).")


class ProcessorTypes:
    """
    Defines the types of data processing available.
    """
    integer = "long"
    line = "line"
    word = "word"


class ProcessorFactory:
    """
    A helper class to create instances of Processor.
    """
    def __init__(self):
        self.processors = {
            ProcessorTypes.integer: IntegerProcessor,
            ProcessorTypes.line: LineProcessor,
            ProcessorTypes.word: WordProcessor,
        }

    def create(self, datatype:str) -> Processor | None:
        """
        Creates and instance of processor if the datatype is valid.
        :param datatype: Represents the type of data to be processed, must be one of the ProcessorTypes.
        :return: A new Processor if datatype is valid, None otherwise.
        """
        if datatype not in self.processors:
            return None

        return self.processors[datatype]()