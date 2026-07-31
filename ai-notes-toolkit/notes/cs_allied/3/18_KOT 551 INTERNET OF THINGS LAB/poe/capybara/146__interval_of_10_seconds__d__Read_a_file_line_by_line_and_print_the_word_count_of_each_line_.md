#### Interval of 10 seconds: Reading files line by line and printing word count

When working with files, it's often necessary to read them line by line and perform certain operations on each line. One common operation is to count the number of words in each line. In this guide, we'll go over how to read a file line by line and print the word count of each line, with a 10-second interval between each line.

Here are the steps to achieve this:

1. Open the file: First, we need to open the file we want to read. We can do this using the `open()` function in Python. For example, to open a file called `example.txt`, we can use the following code:

```
file = open('example.txt', 'r')
```

2. Read the file line by line: Once we have opened the file, we can read it line by line using a `for` loop. For example, we can use the following code to read each line of the file and print it:

```
for line in file:
    print(line)
```

3. Count the words in each line: To count the words in each line, we can use the `split()` function in Python. This function splits a string into a list of words based on whitespace. For example, we can use the following code to count the number of words in a line:

```
num_words = len(line.split())
```

4. Print the word count: Finally, we can print the word count for each line. We can do this within the `for` loop, after counting the words. For example, we can use the following code to print the word count for each line:

```
print('Number of words:', num_words)
```

5. Add a 10-second interval: To add a 10-second interval between each line, we can use the `time.sleep()` function in Python. This function pauses the execution of the program for a specified number of seconds. For example, we can use the following code to add a 10-second interval between each line:

```
import time

for line in file:
    num_words = len(line.split())
    print('Number of words:', num_words)
    time.sleep(10)
```

With these steps, we can read a file line by line, count the number of words in each line, and print the word count with a 10-second interval between each line.