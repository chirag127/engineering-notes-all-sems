# Interval of 10 Seconds: Reading a File Line by Line and Printing Word Count of Each Line

In programming, reading and processing data from a file is a common task. One such task is to read a file line by line and count the number of words in each line. This can be achieved by following these steps:

1. Open the file: To read a file in Python, we first need to open it. This can be done using the `open()` function. For example, to open a file named `example.txt` in read mode, we can use the following code:

```python
file = open("example.txt", "r")
```

2. Read the file line by line: Once the file is opened, we can read its contents line by line using the `readline()` function. This function returns the next line in the file as a string. We can use a loop to read each line in the file. For example:

```python
for line in file:
    # Process each line
    pass
```

3. Count the number of words in each line: To count the number of words in a line, we can split the line into words using the `split()` function. This function splits a string into a list of words based on a given separator. By default, the separator is a space character. We can then count the number of words in the list using the `len()` function. For example:

```python
for line in file:
    words = line.split()
    word_count = len(words)
    print(word_count)
```

4. Close the file: Once we have finished reading the file, we need to close it using the `close()` function. This frees up any system resources used by the file. For example:

```python
file.close()
```

By following these steps, we can read a file line by line and count the number of words in each line. This technique can be useful in a variety of applications, such as text analysis or data processing.