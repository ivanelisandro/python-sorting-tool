from validation import ProcessorOutputs, ProcessorTypes
import sys
import os


class Argument:
    def __init__(self, key:str, value:str, valid_types:list[str], error_message:str):
        self.key = key
        self.value = value
        self.valid_types = valid_types
        self.error_message = error_message

    def is_valid(self, option_value):
        return option_value in self.valid_types


class FileArgument(Argument):
    def __init__(self, key:str, error_message:str, validate_path:bool):
        super().__init__(key, "", [], error_message)
        self.validate_path = validate_path

    def is_valid(self, option_value):
        if not option_value:
            return False
        if self.validate_path:
            return os.path.exists(option_value) and os.path.isfile(option_value)
        return True


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
    input_option = FileArgument(
        "-inputFile",
        "No input file path defined!",
        True)
    output_option = FileArgument(
        "-outputFile",
        "No output file path defined!",
        False)

    def __init__(self):
        self.arguments = sys.argv[1:] if len(sys.argv) > 1 else None
        self.options = {
            self.datatype_option.key : self.datatype_option,
            self.sorting_option.key : self.sorting_option,
            self.input_option.key : self.input_option,
            self.output_option.key : self.output_option,
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
        if not self.options[option].is_valid(option_value):
            print(self.options[option].error_message)
            return

        self.options[option].value = option_value

    def get_options_values(self):
        return self.datatype_option.value, self.sorting_option.value, self.input_option.value, self.output_option.value