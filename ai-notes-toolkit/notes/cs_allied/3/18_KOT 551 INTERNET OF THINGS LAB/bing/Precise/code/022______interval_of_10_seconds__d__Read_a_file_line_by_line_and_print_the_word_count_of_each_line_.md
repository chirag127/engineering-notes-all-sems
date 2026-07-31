#### Interval of 10 seconds
An interval of 10 seconds refers to a time duration or a time period of 10 seconds. This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
To read a file line by line and print the word count of each line, the following steps can be followed:

1. Open the file in read mode.
2. Use a loop to iterate over each line in the file.
3. For each line, use the `split()` function to split the line into a list of words.
4. Use the `len()` function to count the number of words in the list.
5. Print the word count for the current line.
6. Close the file after all lines have been processed.

Here is an example code snippet in Python that demonstrates this process:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```