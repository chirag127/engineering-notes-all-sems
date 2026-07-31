#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as the blinking of an eye, the reaction time of a person, or the frequency of a sound wave.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:

  1. Open the file in read mode and assign it to a variable, such as file.
  2. Initialize a variable, such as line_number, to store the current line number, and set it to 1.
  3. Use a loop, such as a while loop, to iterate over the lines of the file until the end of the file is reached.
  4. For each iteration, read the next line of the file and assign it to a variable, such as line.
  5. Use a built-in function, such as split(), to split the line into a list of words, and assign it to a variable, such as words.
  6. Use another built-in function, such as len(), to get the length of the words list, and assign it to a variable, such as word_count.
  7. Print the line_number, a colon, and the word_count, separated by spaces, to the standard output.
  8. Increment the line_number by 1.
  9. Repeat steps 4 to 8 until the loop condition is false.
  10. Close the file.

- For example, if the file contains the following text:

  ```
  Hello world
  This is a test file
  It has three lines
  ```

- The output of the algorithm would be:

  ```
  1: 2
  2: 5
  3: 4
  ```