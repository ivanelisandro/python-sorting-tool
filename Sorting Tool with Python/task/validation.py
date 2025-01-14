class ProcessorOutputs:
    """
    Defines the types of outputs available.
    """
    summary = "summary"
    sorted = "natural"
    sorted_count = "byCount"
    valid_types = (summary, sorted, sorted_count)


class ProcessorTypes:
    """
    Defines the types of data processing available.
    """
    integer = "long"
    line = "line"
    word = "word"
    valid_types = (integer, line, word)