# Stage 4:

From this stage on, the program will focus on sorting user data, so it will no longer output information about the greatest number or the longest string.

**Objectives:**

Update the parsing of command-line arguments to support the sorting type definition:

- if the `-sortingType` argument is provided, it should be followed by `natural` or `byCount`, which defines the sorting type.
- if the argument is not provided, then consider `natural` to be the default sorting type.

Implement natural sorting for words and lines, and sorting by count for all data types. Within the group, elements with equal count values should be sorted naturally.

**Note:** for strings (words and lines), natural order is lexicographic order, for numbers it is numeric order.

Print the line containing the total number `m` of elements in the input: `Total ELEMENTS: m.`, where `ELEMENTS` can be `numbers`, `words`, or `lines`, depending on the input. Then output the sorting results:

- for natural sorting of numbers or words, print elements on one line in ascending order:

```
Sorted data: el_1 el_2 ... el_m
```

- for natural sorting of lines, print lexicographically sorted elements each on a new line:

```
Sorted data:
line_1
line_2
…
line_m
```

- for sorting by count, print elements sorted by the number of occurrences, each on a new line, using the following format:

```
element: count time(s), percentage%
```

Here, `element` is a number, word, or line, `count` is the number of times it appears in the input, and `percentage` is the proportion of the `count` to the total number of elements in the input, given as a percentage.

## Run configuration examples:

```
python main.py -sortingType natural -dataType long
```

```
python main.py -dataType word -sortingType byCount
```

## Execution examples:

The greater-than symbol followed by a space `>` represents the user input. Note that it's not part of the input.

Example 1, for sorting longs by count:

```
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
-2: 1 time(s), 14%
4: 1 time(s), 14%
33: 1 time(s), 14%
42: 1 time(s), 14%
1: 3 time(s), 43%
```

Example 2, for sorting longs naturally:

```
> 1 -2   33 4
> 42
> 1                 1
Total numbers: 7.
Sorted data: -2 1 1 1 4 33 42 
```

Example 3, for sorting words naturally:

```
> 1 -2   33 4
> 42
> 1                 1
Total words: 7.
Sorted data: -2 1 1 1 33 4 42 
```

Example 4, for sorting lines naturally:

```
> 1 -2   33 4
> 42
> 1                 1
Total lines: 3
Sorted data:
1                 1
1 -2   33 4
42
```
