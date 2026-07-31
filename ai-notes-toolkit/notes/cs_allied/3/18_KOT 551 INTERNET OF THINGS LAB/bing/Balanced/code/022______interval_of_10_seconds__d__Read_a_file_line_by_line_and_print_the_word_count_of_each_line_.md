#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time duration that is equal to 10 units of one second each.
- One second is defined as the time that elapses during 9,192,631,770 cycles of the radiation produced by the transition between two levels of the cesium 133 atom.
- An interval of 10 seconds can be represented by various symbols, such as 10 s, 10 sec, or 10".
- An interval of 10 seconds can be used to measure various phenomena, such as the frequency of sound waves, the speed of a moving object, or the reaction time of a person.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions for file handling and string manipulation.
- The steps to perform this task are as follows:

  1. Open the file in read mode using the `open()` function, which returns a file object.
  2. Loop through the file object using a `for` loop, which iterates over each line of the file as a string.
  3. Split the line string into a list of words using the `split()` method, which separates the string by whitespace characters by default.
  4. Count the number of elements in the list using the `len()` function, which returns an integer value.
  5. Print the word count of the line using the `print()` function, which displays the output to the standard output stream.
  6. Close the file using the `close()` method of the file object, which releases the resources associated with the file.

- An example of Python code that implements this task is as follows:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop through the file line by line
for line in file:
  # Split the line into a list of words
  words = line.split()
  # Count the number of words in the list
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```