## 31. WAP to compare the contents of two files and determine whether they are same or not.

```
import filecmp
def compare_files(file1, file2):
    return filecmp.cmp(file1, file2)

file1 = input("Enter the name of first file: ")
file2 = input("Enter the name of second file: ")

if compare_files(file1, file2):
    print("Files are identical.")
else:
    print("Files are not identical.")
```
