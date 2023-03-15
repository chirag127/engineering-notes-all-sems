### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- A file is a collection of data stored in a disk or a memory device with a specific name and extension.
- Python provides built-in functions and modules to perform various file operations such as opening, closing, reading, writing, appending, deleting, etc.
- Some of the common file operations in Python are:

  - `open(filename, mode)` : This function opens a file with the given name and mode and returns a file object. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, 'r+' for reading and writing, 'b' for binary mode, etc.
  - `close()` : This method closes the file object and frees up any resources associated with it.
  - `read(size)` : This method reads up to size bytes from the file object and returns a string. If size is not specified or negative, it reads the entire file.
  - `write(data)` : This method writes the data string to the file object. It does not add a newline character at the end of the data.
  - `seek(offset, whence)` : This method moves the file pointer to a new position specified by offset relative to whence. The whence can be 0 for the beginning of the file, 1 for the current position, or 2 for the end of the file.
  - `tell()` : This method returns the current position of the file pointer in bytes.
  - `readline()` : This method reads one line from the file object and returns a string. It includes the newline character at the end of the line.
  - `readlines()` : This method reads all the lines from the file object and returns a list of strings. Each string includes the newline character at the end of the line.
  - `writelines(lines)` : This method writes a list of strings to the file object. It does not add any newline characters at the end of the strings.

- Python also provides a module called `os` that contains various functions to perform operating system related tasks such as creating, renaming, deleting, moving, copying, etc. files and directories.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers.
- The Sieve of Eratosthenes is an algorithm that finds all the prime numbers up to a given limit n. It works by creating a list of numbers from 2 to n and marking the multiples of each prime number as composite (not prime), starting from the first prime number 2. The remaining unmarked numbers are prime.
- The steps of the algorithm are:

  - Create a list of numbers from 2 to n and mark them all as unmarked.
  - Set p = 2, the first prime number.
  - Repeat until p^2 > n:
    - Mark all the multiples of p from p^2 to n as marked.
    - Find the next unmarked number greater than p and set it as the new p.
  - The unmarked numbers in the list are the prime numbers up to n.

- The following is an example of the algorithm for n = 20:

  - Create a list of numbers from 2 to 20 and mark them all as unmarked.

    | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
    | - | - | - | - | - | - | - | - | -  | -  | -  | -  | -  | -  | -  | -  | -  | -  | -  |
    | U | U | U | U | U | U | U | U | U  | U  | U  | U  | U  | U  | U  | U  | U  | U  | U  |

  - Set p = 2, the first