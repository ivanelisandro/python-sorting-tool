# Stage 6:

On this stage we will add the option to processing input and output from/to a file.

**Objectives:**

Update command-line arguments parsing to support the `-inputFile` and `-outputFile` arguments.

- If `-inputFile` is provided followed by the file name, read the input data from the file.
- If `-outputFile` is provided followed by the file name, output only the error messages to the console and print the results to the file.

## Execution examples:

Example 1: input file is defined
```
python main.py -sortingType byCount -inputFile input.txt
```

Example 2: input and output files are defined
```
python main.py -sortingType byCount -inputFile data.dat -outputFile out.txt
```
