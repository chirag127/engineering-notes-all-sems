#### Interval of 10 seconds
An interval of 10 seconds refers to a time duration or a time period that lasts for 10 seconds. This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode using a file object.
2. Use a loop to iterate over the file object, which will read the file line by line.
3. For each line, use the `split()` method to split the line into a list of words.
4. Use the `len()` function to find the number of words in the list, which is the word count of the line.
5. Print the word count of the line.
6. Continue the loop until all lines in the file have been read and the word count of each line has been printed.

Here is an example code snippet in Python that demonstrates how to read a file line by line and print the word count of each line:

```python
with open('file.txt', 'r') as file:
    for line in file:
        words = line.split()
        word_count = len(words)
        print(word_count)
```

This code opens the file `file.txt` in read mode, and uses a `for` loop to iterate over the file object. For each line, the `split()` method is used to split the line into a list of words, and the `len()` function is used to find the word count of the line. The word count is then printed using the `print()` function. This process is repeated for all lines in the file.