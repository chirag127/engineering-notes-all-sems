# Interval of 10 seconds: Reading a file line by line and printing word count

In computer programming, reading and processing data from a file is a common task. One way to do this is by reading the file line by line and performing operations on each line. In this case, we will be reading a file and printing the word count of each line.

Here are some key points to keep in mind when implementing this task:

1. The first step is to open the file using the appropriate function, such as `open()` in Python. Make sure to specify the correct file path and mode (e.g. read-only).

2. Once the file is open, you can read it line by line using a loop. One way to do this is using a `while` loop and the `readline()` function. Alternatively, you can use a `for` loop and iterate over the file object directly.

3. For each line, you can use a string function to split it into words. In Python, you can use the `split()` function for this. This will return a list of words, which you can then count using the `len()` function.

4. After counting the words, you can print the result using a formatted string. For example, you can use the `print()` function with the string format specifier `%s` to print the line and the word count.

5. Finally, make sure to close the file using the appropriate function, such as `close()` in Python. This will free up system resources and prevent memory leaks.

Here's an example implementation in Python:

```python
# Open the file for reading
file = open('example.txt', 'r')

# Read the file line by line and print the word count for each line
while True:
    # Read a line from the file
    line = file.readline()

    # Exit the loop if there are no more lines to read
    if not line:
        break

    # Split the line into words and count them
    words = line.split()
    word_count = len(words)

    # Print the line and the word count
    print('%s - %d words' % (line.strip(), word_count))

# Close the file
file.close()
```

Note that this implementation uses a `while` loop and the `readline()` function to read the file line by line. It also uses the `strip()` function to remove any leading or trailing whitespace from the line before printing it. You can modify this code to suit your specific requirements and programming language.