from abc import ABC, abstractmethod


class Processor(ABC):
    """
    Abstract class for processing some type of data.
    """
    @abstractmethod
    def process(self, current_input):
        """
        Abstract method, must be implemented in child class
        """
        pass

    @abstractmethod
    def print_summary(self):
        """
        Abstract method, must be implemented in child class
        """
        pass

class IntegerProcessor(Processor):
    def __init__(self):
        self.numbers = []

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


class StringProcessor(Processor):
    def __init__(self):
        self.contents = []

    def process(self, current_input):
        pass

    def print_summary(self):
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

    def process(self, current_input):
        items = current_input.split()
        for item in items:
            self.contents.append(item)

    def print_summary(self):
        (total, longest, elements, longest_count, rate) = self.calculate_statistics()

        elements.sort()
        print(f"Total words: {total}.")
        print(f"The longest word: {" ".join(elements)} ({longest_count} time(s), {rate}%).")


class ProcessorFactory:
    def __init__(self):
        self.processors = {
            "long": IntegerProcessor,
            "line": LineProcessor,
            "word": WordProcessor,
        }

    def create(self, datatype:str):
        if datatype not in self.processors:
            return None

        return self.processors[datatype]()