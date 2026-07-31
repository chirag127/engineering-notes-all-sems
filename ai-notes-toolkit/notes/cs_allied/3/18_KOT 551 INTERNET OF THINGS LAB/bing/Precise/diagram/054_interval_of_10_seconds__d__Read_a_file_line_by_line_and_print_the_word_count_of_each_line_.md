# Interval of 10 seconds

An interval of 10 seconds refers to a time period or duration of 10 seconds. It can be used in various contexts, such as measuring time between events or setting a timer for a specific task.

# Reading a file line by line and printing the word count of each line

To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode using a file object.
2. Use a loop to iterate over the file object, which will read the file line by line.
3. For each line, use the `split()` method to split the line into a list of words.
4. Use the `len()` function to find the number of words in the list.
5. Print the word count of the line.
6. Close the file object once all lines have been read and processed.

Here is an example code snippet in Python that demonstrates this process:

```python
with open('file.txt', 'r') as file:
    for line in file:
        words = line.split()
        word_count = len(words)
        print(word_count)
```

This code opens the file `file.txt` in read mode, reads it line by line, and prints the word count of each line. The `with` statement is used to ensure that the file is properly closed after it has been read. The `split()` method is used to split each line into a list of words, and the `len()` function is used to find the number of words in the list. Finally, the word count is printed for each line.