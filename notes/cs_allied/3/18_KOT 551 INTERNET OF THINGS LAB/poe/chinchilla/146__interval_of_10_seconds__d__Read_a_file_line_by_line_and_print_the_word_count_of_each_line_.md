#### Interval of 10 seconds: Reading a file line by line and printing the word count of each line

When working with files in Python, it is often necessary to read the contents of a file line by line. In some cases, it may also be necessary to count the number of words in each line. This can be achieved using a few simple lines of code. In this guide, we'll show you how to read a file line by line and print the word count of each line.

Here are the steps to achieve this:

1. Open the file using the `open()` function. This function takes two arguments: the file name and the mode in which to open the file. In this case, we'll be using the read mode `r`. For example:

```
file = open('filename.txt', 'r')
```

2. Loop through the file line by line using a `for` loop. For each line, we'll split the line into words using the `split()` function. This function returns a list of all the words in the line. We'll then use the `len()` function to count the number of words in the line. For example:

```
for line in file:
    words = line.split()
    word_count = len(words)
    print(word_count)
```

3. Close the file using the `close()` function. This is important to ensure that the file is properly closed and resources are freed up. For example:

```
file.close()
```

Putting it all together, here's the complete code to read a file line by line and print the word count of each line:

```python
file = open('filename.txt', 'r')
for line in file:
    words = line.split()
    word_count = len(words)
    print(word_count)
file.close()
```

Note that this code assumes that the file contains only text and that each line is separated by a newline character (`\n`).

In summary, reading a file line by line and printing the word count of each line can be achieved by following these simple steps:

1. Open the file using the `open()` function.
2. Loop through the file line by line using a `for` loop, splitting each line into words and counting the number of words using the `split()` and `len()` functions.
3. Close the file using the `close()` function.