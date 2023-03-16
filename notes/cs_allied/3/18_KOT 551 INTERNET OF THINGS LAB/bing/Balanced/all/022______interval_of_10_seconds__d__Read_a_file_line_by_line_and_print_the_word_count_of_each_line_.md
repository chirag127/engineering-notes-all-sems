#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be represented by various symbols, such as 10 s, 10 sec, or 10".
- An interval of 10 seconds can be used to measure various phenomena, such as the frequency of a sound wave, the speed of a moving object, or the duration of an event.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions and modules for working with files and strings.
- The following steps can be followed to achieve the task:
  - Open the file in read mode using the `open()` function, which returns a file object.
  - Use a `for` loop to iterate over the file object, which yields one line at a time.
  - Use the `split()` method on each line, which returns a list of words separated by whitespace characters.
  - Use the `len()` function on the list, which returns the number of elements in the list, which is equivalent to the word count of the line.
  - Print the word count using the `print()` function, which writes the output to the standard output stream.
  - Close the file using the `close()` method on the file object, which frees up the resources associated with the file.
- The following is an example of Python code that implements the task:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the file object
for line in file:
  # Split the line into a list of words
  words = line.split()
  # Get the word count of the line
  word_count = len(words)
  # Print the word count
  print(word_count)

# Close the file
file.close()
```