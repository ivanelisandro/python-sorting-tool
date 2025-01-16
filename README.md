# Python project: Sorting Tool

This is one of the projects provided by JetBrains Academy, a platform for studying programming languages.

This project consists of a command line application that sorts data:

- You can sort integers, words or lines;
- You can sort them by the "natural" order or "by count"
- Natural order for integers sorts the numbers in increasing order;
- Natural order for text sorts the content by lexicographic order;
- When sorting "by count" the content is sorted by occurrence rate in ascending order;
- You can process data from an input file;
- You can write processed data to an output file;

## Command line arguments

If you don't want to export or import files manually you can specify command line arguments when running the script:

- Use `-dataType someType`, where `someType` must be `long`, `word` or `line`. If not specified the default is `word`;
- Use `-sortingType someOutputType`, where `someOutputType` must be `natural` or `byCount`. If not specified the default is `natural`;
- Use `-inputFile someFileToRead`, where `someFileToRead` must be an existent file. If not specified the default is to use the standard input;
- Use `-outputFile someFileToWrite`, where `someFileToWrite` should be a valid path to write. The output will also always be printed to the standard output, even with the file specified;

The arguments can be used individually or together and the order of the arguments is not important.

### Examples:

```
python main.py -sortingType natural -dataType long
```

```
python main.py -dataType word -sortingType byCount
```

```
python main.py -sortingType byCount -inputFile myFile.txt
```

```
python main.py -sortingType byCount -inputFile myInput.dat -outputFile myOutput.txt
```
