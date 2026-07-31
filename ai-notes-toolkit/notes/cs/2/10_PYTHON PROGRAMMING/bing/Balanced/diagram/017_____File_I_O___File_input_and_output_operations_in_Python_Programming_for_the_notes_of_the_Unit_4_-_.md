### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- A file is a collection of data stored in a disk or memory with a specific name and path.
- Python provides built-in functions and modules to perform various file operations such as opening, closing, reading, writing, appending, deleting, etc.
- Some of the common file operations in Python are:

  - `open(filename, mode)` : Opens a file with the given name and mode and returns a file object. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, 'r+' for reading and writing, 'b' for binary mode, etc.
  - `close()` : Closes the file and frees up any system resources associated with it.
  - `read(size)` : Reads up to size bytes from the file and returns a string. If size is omitted or negative, reads until the end of the file.
  - `write(data)` : Writes the data to the file. The data must be a string or a bytes object.
  - `seek(offset, whence)` : Moves the file pointer to the specified offset from the specified position. The position can be 0 for the beginning of the file, 1 for the current position, or 2 for the end of the file.
  - `tell()` : Returns the current position of the file pointer in bytes.
  - `readline()` : Reads one line from the file and returns a string. If the file is empty or at the end, returns an empty string.
  - `readlines()` : Reads all the lines from the file and returns a list of strings.
  - `writelines(lines)` : Writes a list of strings to the file. Each string is written as a separate line.
  - `with open(filename, mode) as file:` : Creates a context manager that automatically closes the file after the block of code is executed.

- Example of file I/O in Python:

  ```python
  # Writing to a file
  with open("test.txt", "w") as f:
      f.write("Hello, world!\n")
      f.write("This is a test file.\n")

  # Reading from a file
  with open("test.txt", "r") as f:
      data = f.read()
      print(data)
  ```

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers.
- The Sieve of Eratosthenes is an algorithm that finds all the prime numbers up to a given limit n. It works by marking the multiples of each prime number as composite (not prime), starting from the first prime number 2. The remaining unmarked numbers are prime.
- The steps of the algorithm are:

  - Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
  - Let p be the first prime number, starting with 2.
  - Mark all the multiples of p from 2p to n as composite, by crossing them out or setting them to False.
  - Find the first unmarked number greater than p and assign it to p. If there is no such number, stop.
  - Repeat steps 3 and 4 until p is greater than the square root of n.
  - The remaining unmarked numbers are prime.

- Example of the Sieve of Eratosthenes for n = 20:

  | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
  |---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|
  |   |   | X |   | X |   | X | X | X  |    | X  |    | X  | X  | X  |