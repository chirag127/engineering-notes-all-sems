#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- One second is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure various phenomena, such as the frequency of sound waves, the speed of a moving object, or the time elapsed between two events.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions for file handling and string manipulation.
- The steps are as follows:

  1. Open the file in read mode using the `open()` function, which returns a file object.
  2. Loop through the file object using a `for` loop, which iterates over each line of the file.
  3. For each line, use the `split()` method to split the line into a list of words, separated by whitespace characters.
  4. Use the `len()` function to get the length of the list, which is the word count of the line.
  5. Print the word count of the line using the `print()` function, along with the line itself or any other information as desired.
  6. Close the file using the `close()` method of the file object, which frees up the resources associated with the file.

- An example of Python code that implements this task is:

  ```python
  # Open the file in read mode
  file = open("example.txt", "r")

  # Loop through the file object
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