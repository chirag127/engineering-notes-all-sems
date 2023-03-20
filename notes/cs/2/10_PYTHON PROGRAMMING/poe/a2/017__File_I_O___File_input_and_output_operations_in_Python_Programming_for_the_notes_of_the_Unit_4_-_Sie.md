 Here is the formal notes on the given topic in markdown format:

### File I/O : File input and output operations in Python Programming

1.  File Input - To read data from a file, use the open() function to get a file object. Then use the read() or readline() methods on the file object to read data from the file.
2.  File Output - To write data to a file, open the file in write mode ('w'), write to the file using the write() method.
3.  Modes - The mode parameter is used to specify the mode in which the file has to be opened. It can have the following values:
    -   r - Read - Default value. Opens a file for reading, error if the file does not exist
    -   a - Append - Opens a file for appending, creates the file if it does not exist
    -   w - Write - Opens a file for writing, creates the file if it does not exist
    -   x - Create - Creates the specified file, returns an error if the file exists

4.  File Methods - The file object has many methods to manipulate the file, some of them are:
    - read() - Reads the file entirely
    - readline() - Reads a single line from the file
    - write() - Writes the specified string to the file
    - close() - Closes an open file

5. Unit 4 - Sieve of Eratosthenes: An algorithm to generate prime numbers by eliminating multiples of prime numbers. The steps are:
    1.  Take a list of numbers from 2 to n (say 100).
    2.  Mark 2 as prime and cross off all even numbers greater than 2.
    3.  Take the next uncrossed off number (3) and mark it as prime.
    4.  Cross off all multiples of 3.
    5.  Repeat step#3 and #4 until the square root of n.
    6.  The numbers left uncrossed are prime.

The algorithm is named after the Greek Mathematician Eratosthenes.