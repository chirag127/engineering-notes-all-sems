# Interval of 10 seconds

An interval of 10 seconds refers to a time period or duration of 10 seconds. It can be used in various contexts, such as setting a timer, scheduling tasks, or measuring time between events.

# Reading a file line by line and printing the word count of each line

To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode using a file object.
2. Use a loop to iterate over the file object, which will return one line at a time.
3. For each line, use the `split()` method to split the line into a list of words.
4. Use the `len()` function to find the number of words in the list.
5. Print the word count for the current line.
6. Continue iterating over the file object until all lines have been processed.
7. Close the file object.

Here is an example code snippet in Python that demonstrates this process:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```

This code opens the file `file.txt` in read mode, iterates over each line in the file, splits the line into a list of words, finds the word count, and prints it. The `with` statement is used to automatically close the file object when the block of code is finished.