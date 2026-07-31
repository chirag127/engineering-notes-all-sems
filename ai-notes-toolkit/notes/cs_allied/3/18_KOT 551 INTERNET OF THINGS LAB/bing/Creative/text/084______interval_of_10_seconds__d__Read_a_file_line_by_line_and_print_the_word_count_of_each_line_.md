#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as human reaction time, sprinting speed, or heart rate.
- An interval of 10 seconds can also be used to divide a longer period of time into smaller segments, such as a minute, an hour, or a day, for the purpose of counting, timing, or scheduling.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as `file`.
  - Initialize a variable, such as `line_number`, to store the current line number, and set it to 1.
  - Use a loop, such as a `while` loop, to iterate over the lines of the file until the end of the file is reached.
  - For each iteration of the loop, do the following:
    - Read the next line from the file and assign it to a variable, such as `line`.
    - Split the line into a list of words by using a delimiter, such as a space, and assign it to a variable, such as `words`.
    - Count the number of elements in the list of words and assign it to a variable, such as `word_count`.
    - Print the line number, a colon, and the word count, separated by spaces, to the standard output.
    - Increment the line number by 1.
  - Close the file.