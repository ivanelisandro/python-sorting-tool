import sys
from abc import ABC, abstractmethod
from io import StringIO
from validation import ProcessorOutputs, ProcessorTypes
import os


class Processor(ABC):
    """
    Abstract class for processing some type of data.
    """
    def __init__(self, output_type:str, input_path:str, output_path:str):
        self.output_type = output_type
        self.input_path = input_path
        self.output_path = output_path
        self.log = StringIO()
        self.outputs = {
            ProcessorOutputs.summary: self.print_summary,
            ProcessorOutputs.sorted: self.print_sorted,
            ProcessorOutputs.sorted_count: self.print_sorted_count,
        }
        self.item_type = None
        self.superlative = None
        self.items = []

    @abstractmethod
    def process(self, current_input):
        """
        Processes a given line of input.
        """
        pass

    @abstractmethod
    def get_max(self):
        """
        Gets the maximum value of all input content.
        For integers: the greatest number.
        For text: the longest words or lines.
        """
        pass

    @abstractmethod
    def format_max(self):
        """
        Formats the maximum values into a string for output.
        """
        pass

    @abstractmethod
    def get_max_count(self):
        """
        Gets the count of repetitions of the maximum value.
        """
        pass

    @abstractmethod
    def format_sorted(self):
        """
        Formats the sorted output into a string for output.
        """
        pass

    def load_data(self):
        if not self.input_path or not os.path.isfile(self.input_path):
            self.read_from_input()
            return

        self.read_from_file()

    def write_data(self):
        """
        Writes the output data according to the type required by the application.
        """
        if self.output_type in self.outputs:
            self.outputs[self.output_type]()

        if self.output_path:
            with open(self.output_path, "w", encoding="utf-8") as file:
                file.write(self.log.getvalue())


    def write_line(self, line:str):
        """
        Writes a line of output to the processor output_path definition (including a new line at the end)
        :param line: The content to be written.
        """
        print(line)
        print(line, file=self.log)

    def read_from_input(self):
        """
        Reads a line from the standard input and processes it.
        Breaks execution when an EOF character entered by the user.
        """
        while True:
            try:
                data = input()
                self.process(data)
            except EOFError:
                break

    def read_from_file(self):
        """
        Reads all the inputs from a file and processes it.
        :return:
        """
        with open(self.input_path,"r", encoding="utf-8" ) as file:
            for line in file.readlines():
                self.process(line)

    def get_rate(self, counted):
        """
        Calculates the rate of occurrence for a counted item.
        """
        return int(counted * 100 / len(self.items))

    def print_total(self):
        """
        Prints the total number of items being processed.
        :return:
        """
        self.write_line(f"Total {self.item_type}s: {len(self.items)}.")

    def print_summary(self):
        """
        Prints the summarized information of the processed items.
        """
        count = self.get_max_count()
        rate = self.get_rate(count)
        self.print_total()
        print(f"The {self.superlative} {self.item_type}:"
              f"{self.format_max()}"
              f"({count} time(s), {rate}%).")

    def print_sorted(self):
        """
        Prints the sorted items.
        """
        self.print_total()
        self.write_line(f"Sorted data:{self.format_sorted()}")

    def print_sorted_count(self):
        """
        Prints the items sorted by repetition rate.
        """
        self.print_total()
        unique_elements = set(self.items)
        counted_elements = [(self.items.count(element), element) for element in unique_elements]
        counted_elements.sort()

        for count, element in counted_elements:
            self.write_line(f"{element}: {count} time(s), {self.get_rate(count)}%")


class IntegerProcessor(Processor):
    """
    Specific processor for sorting integer data.
    """
    def __init__(self, output_type:str, input_path:str, output_path:str):
        super().__init__(output_type, input_path, output_path)
        self.item_type = "number"
        self.superlative = "greatest"

    def process(self, current_input):
        input_items = current_input.split()
        for item in input_items:
            try:
                number = int(item)
                self.items.append(number)
            except ValueError:
                self.write_line(f"\"{item}\" is not a long. It will be skipped.")


    def get_max(self):
        return max(self.items)

    def format_max(self):
        return f" {self.get_max()} "

    def get_max_count(self):
        return self.items.count(self.get_max())

    def format_sorted(self):
        self.items.sort()
        formatted_items = " ".join(str(number) for number in self.items)
        return f" {formatted_items}"


class StringProcessor(Processor):
    """
    Specific processor for common text data.
    """
    def __init__(self, output_type:str, input_path:str, output_path:str):
        super().__init__(output_type, input_path, output_path)
        self.superlative = "longest"

    def process(self, current_input):
        pass

    def get_max(self):
        longest_size = max([len(text) for text in self.items])
        return [text for text in self.items if len(text) == longest_size]

    def format_max(self):
        pass

    def get_max_count(self):
        return len(self.get_max())

    def format_sorted(self):
        pass


class LineProcessor(StringProcessor):
    """
    Specific processor for sorting lines of text.
    """
    def __init__(self, output_type:str, input_path:str, output_path:str):
        super().__init__(output_type, input_path, output_path)
        self.item_type = "line"

    def process(self, current_input):
        self.items.append(current_input)

    def format_max(self):
        elements = self.get_max()
        elements.sort()
        formatted_elements = "\n".join(elements)
        return f"\n{formatted_elements}\n"

    def format_sorted(self):
        self.items.sort()
        formatted_items = "\n".join(self.items)
        return f"\n{formatted_items}"


class WordProcessor(StringProcessor):
    """
    Specific processor for sorting words from the input.
    """
    def __init__(self, output_type:str, input_path:str, output_path:str):
        super().__init__(output_type, input_path, output_path)
        self.item_type = "word"

    def process(self, current_input):
        input_items = current_input.split()
        for item in input_items:
            self.items.append(item)

    def format_max(self):
        elements = self.get_max()
        elements.sort()
        formatted_elements = " ".join(elements)
        return f" {formatted_elements} "

    def format_sorted(self):
        self.items.sort()
        formatted_items = " ".join(self.items)
        return f" {formatted_items}"


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

    def create(self, datatype:str, output_type:str, input_path:str, output_path:str) -> Processor | None:
        """
        Creates and instance of processor if the datatype is valid.
        :param datatype: Represents the type of data to be processed, must be one of the ProcessorTypes.
        :param input_path: Represents a file path to read the input from. If empty, the standard input is used.
        :param output_path: Represents a file path to write the output to. If empty, the standard output is used.
        :param output_path: Represents a file path to write the output to. If empty, the standard output is used.
        :param output_type: Must be one of the ProcessorOutputs.
        :return: A new Processor if datatype is valid, None otherwise.
        """
        if datatype not in self.processors:
            return None

        return self.processors[datatype](output_type, input_path, output_path)