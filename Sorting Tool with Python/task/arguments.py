from validation import ProcessorOutputs, ProcessorTypes
import sys


class Argument:
    def __init__(self, key:str, value:str, valid_types:list[str], error_message:str):
        self.key = key
        self.value = value
        self.valid_types = valid_types
        self.error_message = error_message


class ArgumentParser:
    datatype_option = Argument(
        "-dataType",
        ProcessorTypes.word,
        ProcessorTypes.valid_types,
        "No data type defined!")
    sorting_option = Argument(
        "-sortingType",
        ProcessorOutputs.sorted,
        ProcessorOutputs.valid_types,
        "No sorting type defined!")

    def __init__(self):
        self.arguments = sys.argv[1:] if len(sys.argv) > 1 else None
        self.options = {
            self.datatype_option.key : self.datatype_option,
            self.sorting_option.key : self.sorting_option,
        }

    def process(self):
        if not self.arguments:
            return

        for index, argument in enumerate(self.arguments):
            if argument in self.options:
                self.set_option(index, argument)
            if argument.startswith("-") and argument not in self.options:
                print(f"\"{argument}\" is not a valid parameter. It will be skipped.")

    def set_option(self, current_index, option):
        option_value_index = current_index + 1
        if option_value_index >= len(self.arguments):
            self.options[option].value = None
            print(self.options[option].error_message)
            return

        option_value = self.arguments[option_value_index]
        if option_value not in self.options[option].valid_types:
            print(self.options[option].error_message)
            return

        self.options[option].value = option_value

    def get_options_values(self):
        return self.datatype_option.value, self.sorting_option.value