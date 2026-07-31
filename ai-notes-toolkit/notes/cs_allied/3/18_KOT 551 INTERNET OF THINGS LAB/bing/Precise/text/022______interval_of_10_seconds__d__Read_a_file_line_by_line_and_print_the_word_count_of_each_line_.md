#### Interval of 10 seconds
- An interval of 10 seconds refers to a time duration or a time period of 10 seconds.
- This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python.
- In Python, this can be achieved by opening the file in read mode and using a for loop to iterate over each line in the file.
- The `split()` function can be used to split each line into a list of words, and the `len()` function can be used to count the number of words in the list.
- The word count of each line can then be printed using the `print()` function.
- Here is an example code snippet that demonstrates this:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```