#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time duration that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be represented in various ways, such as 10 s, 10 sec, 0.1667 min, 0.0028 h, etc.
- An interval of 10 seconds can be used to measure the frequency of events that occur at a rate of 0.1 Hz, such as the blinking of a human eye, the rotation of a ceiling fan, or the ticking of a clock.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions and modules for file handling and text processing.
- The following steps can be followed to achieve the task:
  - Open the file in read mode using the `open()` function, which returns a file object.
  - Use a `for` loop to iterate over the file object, which yields one line at a time as a string.
  - Use the `split()` method to split the line into a list of words, separated by whitespace characters such as spaces, tabs, or newlines.
  - Use the `len()` function to get the number of elements in the list, which is the word count of the line.
  - Print the word count of the line using the `print()` function, along with the line itself or any other information as desired.
  - Close the file using the `close()` method of the file object, which frees up the resources associated with the file.
- The following is an example of Python code that implements the above steps:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the file object
for line in file:
  # Split the line into a list of words
  words = line.split()
  # Get the word count of the line
  word_count = len(words)
  # Print the word count and the line
  print(word_count, line)

# Close the file
file.close()
```