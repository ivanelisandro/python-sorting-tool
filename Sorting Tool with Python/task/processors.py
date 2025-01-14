from abc import ABC, abstractmethod
from validation import ProcessorOutputs, ProcessorTypes


class Processor(ABC):
    """
    Abstract class for processing some type of data.
    """
    def __init__(self):
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
        Abstract method, must be implemented in child class.
        """
        pass

    @abstractmethod
    def get_max(self):
        """
        Abstract method, must be implemented in child class.
        """
        pass

    @abstractmethod
    def format_max(self):
        """
        Abstract method, must be implemented in child class.
        """
        pass

    @abstractmethod
    def get_max_count(self):
        """
        Abstract method, must be implemented in child class.
        """
        pass

    @abstractmethod
    def format_sorted(self):
        """
        Abstract method, must be implemented in child class.
        """
        pass

    def get_rate(self, counted):
        """
        Calculates the rate of occurrence for a counted item.
        """
        return int(counted * 100 / len(self.items))

    def print(self, output_type:str):
        """
        Prints the output according to the type required by the application.
        :param output_type: Must be one of the ProcessorOutputs.
        """
        if output_type in self.outputs:
            self.outputs[output_type]()

    def print_total(self):
        """
        Prints the total number of items being processed.
        :return:
        """
        print(f"Total {self.item_type}s: {len(self.items)}.")

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
        print(f"Sorted data:{self.format_sorted()}")

    def print_sorted_count(self):
        """
        Prints the items sorted by repetition rate.
        """
        self.print_total()
        unique_elements = set(self.items)
        counted_elements = [(self.items.count(element), element) for element in unique_elements]
        counted_elements.sort()

        for count, element in counted_elements:
            print(f"{element}: {count} time(s), {self.get_rate(count)}%")


class IntegerProcessor(Processor):
    """
    Specific processor for sorting integer data.
    """
    def __init__(self):
        super().__init__()
        self.item_type = "number"
        self.superlative = "greatest"

    def process(self, current_input):
        input_items = current_input.split()
        for item in input_items:
            try:
                number = int(item)
                self.items.append(number)
            except ValueError:
                print(f"\"{item}\" is not a long. It will be skipped.")


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
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
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

    def create(self, datatype:str) -> Processor | None:
        """
        Creates and instance of processor if the datatype is valid.
        :param datatype: Represents the type of data to be processed, must be one of the ProcessorTypes.
        :return: A new Processor if datatype is valid, None otherwise.
        """
        if datatype not in self.processors:
            return None

        return self.processors[datatype]()