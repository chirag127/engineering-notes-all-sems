#### Interval of 10 seconds: Reading a file line by line and printing the word count of each line

In computer programming, it is often necessary to read files for various purposes. One common task is to read a file line by line and perform a certain operation on each line. In this case, we want to read a file and print the word count of each line.

Here are the steps to accomplish this task:

1. Open the file: To read a file, we first need to open it using the `open()` function. This function takes two parameters: the file name and the mode in which we want to open the file. In this case, we will use the mode `r`, which stands for "read". 

   ```python
   file = open("filename.txt", "r")
   ```

2. Read the file line by line: Once the file is opened, we can read it line by line using a loop. In Python, we can use a `for` loop to iterate over the lines in the file. 

   ```python
   for line in file:
       # Perform operation on the line
   ```

3. Count the words in each line: To count the words in a line, we can use the `split()` method, which splits a string into a list of words. We can then use the `len()` function to get the number of words in the list. 

   ```python
   word_count = len(line.split())
   ```

4. Print the word count: Finally, we can print the word count of each line using the `print()` function. To display the line number along with the word count, we can use a counter variable and increment it in each iteration of the loop. 

   ```python
   count = 1
   for line in file:
       word_count = len(line.split())
       print("Line", count, "has", word_count, "words")
       count += 1
   ```

5. Close the file: After we have finished reading the file, it is important to close it using the `close()` method to free up system resources. 

   ```python
   file.close()
   ```

Putting it all together, the complete code for reading a file line by line and printing the word count of each line looks like this:

```python
file = open("filename.txt", "r")
count = 1
for line in file:
    word_count = len(line.split())
    print("Line", count, "has", word_count, "words")
    count += 1
file.close()
```

Note that in this example, we assume that each line in the file contains text. If there are blank lines, or lines with only whitespace, the word count will be zero. Also, if there are lines that are too long, the `split()` method may not work correctly and the word count may be inaccurate.