### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- A file is a collection of data stored in a disk or memory with a specific name and extension.
- Python provides built-in functions and modules to handle various types of files, such as text files, binary files, CSV files, JSON files, etc.
- To perform file I/O operations in Python, we need to follow these steps:
  - Open the file using the `open()` function, which returns a file object.
  - Perform the desired read or write operations using the file object's methods, such as `read()`, `write()`, `readline()`, `writelines()`, etc.
  - Close the file using the `close()` method of the file object, which releases the resources associated with the file.

- The `open()` function takes two parameters: the file name and the mode. The mode specifies how the file is opened and what operations are allowed on it. Some common modes are:
  - `'r'` : read mode, opens the file for reading only, raises an error if the file does not exist.
  - `'w'` : write mode, opens the file for writing only, creates the file if it does not exist, truncates the file if it exists.
  - `'a'` : append mode, opens the file for writing only, creates the file if it does not exist, writes at the end of the file if it exists.
  - `'r+'` : read and write mode, opens the file for both reading and writing, raises an error if the file does not exist.
  - `'w+'` : read and write mode, opens the file for both reading and writing, creates the file if it does not exist, truncates the file if it exists.
  - `'a+'` : read and write mode, opens the file for both reading and writing, creates the file if it does not exist, writes at the end of the file if it exists.
  - `'b'` : binary mode, opens the file as a binary file, which means the data is read and written in bytes.
  - `'t'` : text mode, opens the file as a text file, which means the data is read and written in strings. This is the default mode if not specified.

- The file object's methods can be used to perform various operations on the file, such as:
  - `read(size)` : reads up to `size` bytes or characters from the file and returns them as a string or bytes object. If `size` is not specified or negative, reads the entire file.
  - `write(data)` : writes the data (string or bytes) to the file and returns the number of bytes or characters written.
  - `readline(size)` : reads one line from the file and returns it as a string or bytes object. If `size` is specified, reads up to `size` bytes or characters from the line. If the end of the file is reached, returns an empty string or bytes object.
  - `writelines(lines)` : writes a list of lines (strings or bytes) to the file, without adding any newline characters.
  - `seek(offset, whence)` : moves the file pointer to a new position, where `offset` is the number of bytes or characters to move, and `whence` is the reference point, which can be 0 (start of the file), 1 (current position), or 2 (end of the file).
  - `tell()` : returns the current position of the file pointer in bytes or characters.
  - `flush()` : flushes the write buffer of the file object, which means the data is written to the disk immediately.
  - `close()` : closes the file object and releases the resources associated with it.

- Here is an example of file I/O operations in Python:

```python
# open a text file for writing
f = open("example.txt", "w")

# write some lines to the file
f.write("This is the first line.\n")
f.write("This is the second line.\n")
f.writelines(["This is the third line.\n", "This is the fourth line.\n"])

# close the file
f.close()

# open the same file for reading
f = open("example.txt", "r")

# read the entire file
data = f.read()
print(data)

# read the first line