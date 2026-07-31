## 31. WAP to compare the contents of two files and determine whether they are same or not.

Here is a program that compares the contents of two files and determines whether they are the same or not:

```python
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            print("The contents of the two files are the same.")
        else:
            print("The contents of the two files are different.")
```

This program defines a function `compare_files` that takes two arguments: `file1` and `file2`, which are the names of the two files to be compared. The function opens both files in read mode using the `with` statement and the `open` function. The contents of the files are read using the `read` method and stored in the variables `content1` and `content2`. The `if` statement is used to compare the contents of the two files. If the contents are the same, a message is printed indicating that the contents of the two files are the same. Otherwise, a message is printed indicating that the contents of the two files are different.

To use this function, you can call it and pass the names of the two files you want to compare as arguments. For example:

```python
compare_files('file1.txt', 'file2.txt')
```

This will compare the contents of the files `file1.txt` and `file2.txt` and print a message indicating whether the contents of the two files are the same or different.