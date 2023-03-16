#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as human reaction time, sprinting speed, or heart rate.
- An interval of 10 seconds can also be used to divide a longer period of time into smaller segments, such as counting down to a launch, setting a timer, or performing an exercise routine.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as file.
  - Initialize a variable, such as line_number, to store the current line number, and set it to 1.
  - Use a loop, such as a while loop, to iterate over the file until the end of the file is reached.
    - In each iteration, read the next line from the file and assign it to a variable, such as line.
    - Use a built-in function, such as len(), to count the number of words in the line by splitting the line by whitespace characters and taking the length of the resulting list.
    - Print the line number and the word count, separated by a colon, to the standard output.
    - Increment the line number by 1.
  - Close the file.
- For example, if the file contains the following text:

```
This is a sample file
It has four lines
Each line has a different number of words
The last line is the longest
```
- The output of the algorithm would be:

```
1: 5
2: 4
3: 7
4: 6
```