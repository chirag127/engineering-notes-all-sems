#### Interval of 10 seconds
- An interval of 10 seconds refers to a time period or duration of 10 seconds.
- This interval can be used in various contexts, such as setting a timer, scheduling a task, or measuring the time between two events.

#### Read a file line by line and print the word count of each line
- To read a file line by line, you can use a loop to iterate over each line in the file.
- For each line, you can use the `split()` method to split the line into a list of words.
- The length of this list represents the word count of the line.
- You can then print the word count of each line as you iterate through the file.

Here is an example of how this can be done in Python:

```python
with open('file.txt', 'r') as f:
    for line in f:
        words = line.split()
        word_count = len(words)
        print(word_count)
```