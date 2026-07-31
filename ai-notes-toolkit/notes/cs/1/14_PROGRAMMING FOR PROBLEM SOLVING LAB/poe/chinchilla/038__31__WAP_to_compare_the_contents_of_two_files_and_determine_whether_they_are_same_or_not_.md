## 31. WAP to compare the contents of two files and determine whether they are same or not.

When working with files in programming, it is often necessary to compare the contents of two files to determine if they are the same or not. This can be achieved using a simple program that compares the contents of two files and returns a boolean value indicating whether they are the same or not. Here are the steps to create such a program:

1. Open the first file: The first step is to open the first file that you want to compare. This can be done using the open() function in Python. You will need to specify the file path and the mode in which you want to open the file (read, write, append, etc.).

2. Read the contents of the first file: Once you have opened the first file, you can read its contents using the read() function. This will return the entire contents of the file as a string.

3. Open the second file: Next, you need to open the second file that you want to compare. Again, you can use the open() function to do this.

4. Read the contents of the second file: Once you have opened the second file, you can read its contents using the read() function, just like you did with the first file.

5. Compare the contents of the two files: Now that you have the contents of both files as strings, you can compare them using the == operator. This will return a boolean value indicating whether the two strings are the same or not.

6. Close the files: Finally, you should close both files to free up system resources. This can be done using the close() function.

Here is an example program that implements the above steps:

```python
def compare_files(file1, file2):
    with open(file1, 'r') as f1:
        contents1 = f1.read()
    with open(file2, 'r') as f2:
        contents2 = f2.read()
    return contents1 == contents2
```

In this program, the compare_files() function takes two file paths as arguments and returns a boolean value indicating whether the contents of the two files are the same or not. The function uses the with statement to automatically close the files when it is done with them.

To use this program, simply call the compare_files() function with the paths of the two files you want to compare. For example:

```python
result = compare_files('file1.txt', 'file2.txt')
if result:
    print('The files are the same')
else:
    print('The files are different')
```

This code will compare the contents of 'file1.txt' and 'file2.txt' and print either "The files are the same" or "The files are different" depending on the result.