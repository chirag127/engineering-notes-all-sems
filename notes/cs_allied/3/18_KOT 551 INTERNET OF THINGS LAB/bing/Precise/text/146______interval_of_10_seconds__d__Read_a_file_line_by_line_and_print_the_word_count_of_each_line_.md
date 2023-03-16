#### Interval of 10 seconds
- An interval of 10 seconds refers to a time duration or a time period of 10 seconds.
- This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
- To read a file line by line, one can use a loop to iterate over each line in the file.
- The word count of each line can be obtained by splitting the line into words using a delimiter (such as space) and counting the number of words.
- The word count of each line can then be printed using a print statement within the loop.
- Here is an example code snippet in Python that demonstrates this:

```python
with open('file.txt', 'r') as file:
    for line in file:
        words = line.split()
        word_count = len(words)
        print(f'Word count: {word_count}')
```