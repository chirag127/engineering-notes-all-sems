#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as the reaction time of a person, the frequency of a sound wave, or the speed of a moving object.
- An interval of 10 seconds can also be used to divide a longer period of time into smaller segments, such as a minute, an hour, or a day. For example, a minute has 6 intervals of 10 seconds, an hour has 360 intervals of 10 seconds, and a day has 8,640 intervals of 10 seconds.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as `file`.
  - Initialize a variable, such as `line_number`, to store the current line number, and set it to 1.
  - Use a loop, such as a `while` loop, to iterate over the lines of the file until the end of the file is reached.
    - In each iteration, read the next line of the file and assign it to a variable, such as `line`.
    - Use a function, such as `split()`, to split the line into a list of words, and assign it to a variable, such as `words`.
    - Use a function, such as `len()`, to get the length of the list of words, and assign it to a variable, such as `word_count`.
    - Print the line number, the line, and the word count, separated by commas or other delimiters, such as `print(line_number, line, word_count)`.
    - Increment the line number by 1, such as `line_number += 1`.
  - Close the file, such as `file.close()`.
- For example, if the file contains the following text:

```
This is the first line.
This is the second line, with more words.
This is the third and final line.
```

- The output of the algorithm would be:

```
1, This is the first line., 5
2, This is the second line, with more words., 8
3, This is the third and final line., 6
```