#### Interval of 10 seconds
- An interval of 10 seconds refers to a time period or duration of 10 seconds.
- This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, you can use a programming language such as Python.
- In Python, you can open a file using the `open()` function and read its contents line by line using a `for` loop.
- For each line, you can use the `split()` method to split the line into a list of words, and then use the `len()` function to count the number of words in the list.
- You can then print the word count for each line using the `print()` function.
- Here is an example code snippet that demonstrates this process:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```
- This code opens a file named `file.txt` in read mode, reads its contents line by line, counts the number of words in each line, and prints the word count for each line.