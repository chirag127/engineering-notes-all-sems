#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be written as 10 s or 10 sec in SI notation, or as 0:00:10 in hh:mm:ss format.
- An interval of 10 seconds can be used to measure short durations of events or processes, such as the reaction time of a person, the frequency of a sound wave, or the speed of a moving object.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions and modules for working with files and strings.
- The following steps can be followed to achieve this task in Python:

  1. Open the file in read mode using the `open()` function, which returns a file object.
  2. Use a `for` loop to iterate over the file object, which yields one line at a time as a string.
  3. Use the `split()` method on the line string, which returns a list of words separated by whitespace characters.
  4. Use the `len()` function on the list, which returns the number of elements in the list, which is the word count of the line.
  5. Use the `print()` function to display the word count of the line, along with the line itself or any other information as desired.
  6. Close the file using the `close()` method on the file object, which frees up the resources associated with the file.

- The following is an example of Python code that implements this task, assuming the file name is `text.txt` and it contains some text:

  ```python
  # Open the file in read mode
  file = open("text.txt", "r")

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