# Reading a File Line by Line and Counting Words

When working with text data, it is often necessary to read data from a file and perform some operations on it. One common task is to read a file line by line and count the number of words in each line. This can be done easily in Python using a few simple steps.

## Steps to Read a File Line by Line and Count Words

1. Open the file: Use the `open()` function to open the file in read mode. Specify the file path as an argument to the function.

   ```python
   file = open('file.txt', 'r')
   ```

2. Read the file line by line: Use a `for` loop to iterate over each line in the file. For each line, use the `split()` method to split the line into words and count the number of words using the `len()` function.

   ```python
   for line in file:
       word_count = len(line.split())
       print(word_count)
   ```

3. Close the file: After reading the file, it is important to close the file using the `close()` method to free up system resources.

   ```python
   file.close()
   ```

## Example

Suppose we have a text file `example.txt` with the following contents:

```
This is the first line.
This is the second line with more words.
And this is the third line with even more words than the second line.
```

We can read the file line by line and count the number of words in each line using the following code:

```python
file = open('example.txt', 'r')

for line in file:
    word_count = len(line.split())
    print(word_count)

file.close()
```

The output of this code will be:

```
5
7
12
```

This means that the first line has 5 words, the second line has 7 words, and the third line has 12 words.

## Conclusion

Reading a file line by line and counting the number of words in each line is a common task in text processing. With the steps outlined above, this can be done easily in Python.