Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to compare the contents of two files and determine whether they are same or not. Here is the content in markdown format:

## 31. WAP to compare the contents of two files and determine whether they are same or not.

- To compare the contents of two files, we need to open both files in read mode and read their contents line by line.
- We can use a loop to iterate over the lines of both files and compare them using the `==` operator.
- If any line is different, we can break the loop and print that the files are not same.
- If the loop ends without breaking, we can print that the files are same.
- We also need to handle the possible exceptions that may occur while opening or reading the files, such as `FileNotFoundError` or `IOError`.
- Here is an example of the program in Python:

```python
# Open the first file in read mode
try:
    file1 = open("file1.txt", "r")
except FileNotFoundError:
    print("File1 not found")
    exit()

# Open the second file in read mode
try:
    file2 = open("file2.txt", "r")
except FileNotFoundError:
    print("File2 not found")
    exit()

# Initialize a flag to indicate if the files are same or not
same = True

# Loop over the lines of both files
for line1, line2 in zip(file1, file2):
    # Compare the lines
    if line1 != line2:
        # If different, set the flag to False and break the loop
        same = False
        break

# Close the files
file1.close()
file2.close()

# Print the result based on the flag
if same:
    print("The files are same")
else:
    print("The files are not same")
```