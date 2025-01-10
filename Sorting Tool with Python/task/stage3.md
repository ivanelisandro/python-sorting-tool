# Stage 3:

Focus on stage 3 is adding the capacity for the script to sort integers

**Objectives:**

Update the parsing of command-line arguments to support the number sorting option.

- If the `-sortIntegers` argument is provided, ignore the other arguments and output two lines: the first containing the total number of numbers in the input, and the second containing all of the input numbers in ascending order.
- If the `-sortIntegers` argument is not provided, the behavior of the program should be the same as in the previous stage.

## Run configuration examples:

```
python main.py -sortIntegers
```

## Execution examples:

The greater-than symbol followed by a space `>` represents the user input. Note that it's not part of the input.

```
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
Sorted data: -2 1 1 1 4 33 42
```
