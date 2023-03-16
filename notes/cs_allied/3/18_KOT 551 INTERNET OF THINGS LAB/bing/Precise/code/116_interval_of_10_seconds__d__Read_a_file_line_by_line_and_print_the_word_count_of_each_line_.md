# Interval of 10 seconds

An interval of 10 seconds refers to a time duration or time period of 10 seconds. It can be used in various contexts such as measuring time, setting timers, scheduling tasks, etc.

# Reading a file line by line and printing the word count of each line

To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode using a file object.
2. Use a loop to iterate over the file object. This will read the file line by line.
3. For each line, use the `split()` method to split the line into a list of words.
4. Use the `len()` function to find the number of words in the list.
5. Print the word count of the line.
6. Close the file object after all lines have been read and processed.

Here is an example code snippet in Python that demonstrates the above steps:

```python
# Open the file in read mode
with open('file.txt', 'r') as file:
    # Iterate over the file object line by line
    for line in file:
        # Split the line into a list of words
        words = line.split()
        # Find the number of words in the list
        word_count = len(words)
        # Print the word count of the line
        print(word_count)
```

This code will read the file `file.txt` line by line and print the word count of each line. The file object is opened using the `with` statement, which ensures that the file is properly closed after all lines have been read and processed. The `split()` method is used to split each line into a list of words, and the `len()` function is used to find the number of words in the list. The word count of each line is then printed using the `print()` function.