 Here is the formal content on the given topic:

#### Interval of 10 seconds

a) Import the time module.
b) Use the sleep() function to introduce an delay of 10 seconds.
c) Within the delay, no other tasks can be performed. The control will resume after 10 seconds.
d) The sleep() function takes seconds as the input.

Examples:
import time
time.sleep(10)  # delays the execution for 10 seconds

print("Done")

This will print "Done" after 10 seconds of delay.

d) Read a file line by line and print the word count of each line:

- Open the file in read mode
- Use a for loop to iterate over the file object
- Split each line into words using .split() method
- Count the number of words in each line using len() function
- Print the word count of each line

Example:
f = open("file.txt", "r")
for line in f:
    words = line.split()
    print(len(words))

f.close()

This will print the word count of each line in the given file.