#### Interval of 10 Seconds: Reading a File Line by Line and Printing Word Count of Each Line

When working with large files, it's important to have efficient ways to read and process the data. In this topic, we'll discuss how to read a file line by line and print the word count of each line. This can be useful in a variety of applications, such as text analysis or data processing.

Here are the steps to accomplish this task:

1. Open the file: To begin, we need to open the file we want to read. We can use the built-in `open()` function to do this. 

```python
file = open('filename.txt', 'r')
```

2. Read the file line by line: Once the file is opened, we can read it line by line using a loop. The `readline()` function reads one line at a time and returns it as a string. We can then process this string as needed.

```python
for line in file:
    # process the line
```

3. Split the line into words: To count the number of words in each line, we first need to split the line into individual words. We can use the `split()` function to do this. This function splits a string into a list of words based on a delimiter (by default, whitespace).

```python
words = line.split()
```

4. Count the words: Once we have a list of words, we can count the number of items in the list to get the word count.

```python
word_count = len(words)
```

5. Print the word count: Finally, we can print the word count for each line. We can use the `print()` function to do this.

```python
print(f"Line {line_num}: {word_count} words")
```

Putting it all together, here's the complete code to read a file line by line and print the word count of each line:

```python
file = open('filename.txt', 'r')
line_num = 0
for line in file:
    line_num += 1
    words = line.split()
    word_count = len(words)
    print(f"Line {line_num}: {word_count} words")
file.close()
```

With this code, we can easily process large files and get insights into the data they contain. By reading the file line by line, we can also conserve memory and avoid overloading the system.