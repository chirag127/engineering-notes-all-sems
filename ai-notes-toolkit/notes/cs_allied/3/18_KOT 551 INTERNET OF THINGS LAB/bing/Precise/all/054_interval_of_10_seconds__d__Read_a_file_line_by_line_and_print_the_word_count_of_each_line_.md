# Interval of 10 seconds

An interval of 10 seconds refers to a time period or duration of 10 seconds. It can be used in various contexts, such as measuring time, setting timers, or scheduling events.

# Reading a file line by line and printing the word count of each line

To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode using a file object.
2. Use a loop to iterate over the lines in the file.
3. For each line, use the `split()` method to split the line into a list of words.
4. Use the `len()` function to find the number of words in the list.
5. Print the word count for the current line.
6. Close the file object once all lines have been processed.

Here is an example of how this can be implemented in Python:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```

This code opens the file `file.txt` in read mode, iterates over each line in the file, splits the line into a list of words, finds the word count, and prints it. Once all lines have been processed, the file object is closed.