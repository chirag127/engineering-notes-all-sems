#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events, processes, or phenomena that occur or change within that time span.
- For example, an interval of 10 seconds can be used to measure the frequency of a sound wave, the speed of a moving object, the reaction time of a person, or the blinking rate of an LED.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as file.
  - Initialize a variable, such as line_number, to store the current line number, and set it to 1.
  - Use a loop, such as a while loop, to iterate over the lines of the file until the end of the file is reached.
  - For each iteration, read the next line of the file and assign it to a variable, such as line.
  - Split the line into a list of words, such as by using the split() method, and assign it to a variable, such as words.
  - Count the number of elements in the words list and assign it to a variable, such as word_count.
  - Print the line_number, the line, and the word_count, separated by commas or other delimiters, such as by using the print() function.
  - Increment the line_number by 1.
  - Close the file after the loop is finished, such as by using the close() method.
- For example, if the file contains the following text:

```
Hello, world!
This is a test file.
It has three lines and 11 words.
```

- The output of the algorithm would be:

```
1, Hello, world!, 2
2, This is a test file., 5
3, It has three lines and 11 words., 6
```