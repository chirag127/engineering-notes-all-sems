#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be represented by various symbols, such as 10 s, 10 sec, or 10".
- An interval of 10 seconds can be used to measure the duration of events, such as the time it takes for a pendulum to swing back and forth, the time it takes for a sound wave to travel a certain distance, or the time it takes for a chemical reaction to occur.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions and modules for working with files and strings.
- A possible algorithm for this task is as follows:

  1. Open the file in read mode using the `open()` function, which returns a file object.
  2. Loop through the file object using a `for` loop, which iterates over each line of the file as a string.
  3. Split the line into a list of words using the `split()` method, which separates the string by whitespace characters by default.
  4. Get the length of the list using the `len()` function, which returns the number of elements in the list.
  5. Print the length of the list using the `print()` function, which displays the output to the standard output stream.
  6. Close the file using the `close()` method, which frees up the resources associated with the file object.

- A possible code example for this task in Python is as follows:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop through the file object
for line in file:
  # Split the line into a list of words
  words = line.split()
  # Get the length of the list
  word_count = len(words)
  # Print the length of the list
  print(word_count)

# Close the file
file.close()
```