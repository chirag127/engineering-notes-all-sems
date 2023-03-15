## 31. WAP to compare the contents of two files and determine whether they are same or not.

To compare the contents of two files and determine whether they are the same or not, you can use the following steps:

1. Open the two files in read mode.
2. Read the contents of the first file and store it in a variable.
3. Read the contents of the second file and store it in another variable.
4. Compare the contents of the two variables.
5. If the contents are the same, print that the files are the same.
6. If the contents are different, print that the files are different.
7. Close the files.

Here is an example code in Python that implements the above steps:

```python
# Open the two files in read mode
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

# Read the contents of the first file and store it in a variable
file1_contents = file1.read()

# Read the contents of the second file and store it in another variable
file2_contents = file2.read()

# Compare the contents of the two variables
if file1_contents == file2_contents:
    print('The files are the same.')
else:
    print('The files are different.')

# Close the files
file1.close()
file2.close()
```

This code opens the two files `file1.txt` and `file2.txt` in read mode, reads their contents, and stores them in the variables `file1_contents` and `file2_contents`, respectively. It then compares the contents of the two variables using the `==` operator. If the contents are the same, it prints that the files are the same. Otherwise, it prints that the files are different. Finally, it closes the files.