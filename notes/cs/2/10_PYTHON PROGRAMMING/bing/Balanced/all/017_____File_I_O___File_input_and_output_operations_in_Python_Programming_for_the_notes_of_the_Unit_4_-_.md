# File I/O: File input and output operations in Python Programming

- File input and output in Python is to get input in a program from a file and write output to the same or another file.
- Python provides some built-in functions to perform both input and output operations, such as `print()`, `input()`, `open()`, `read()`, `write()`, and `close()`.
- To open a file in Python, we use the `open()` function, which takes two arguments: the file name and the mode  .
- The mode specifies how we want to access the file, such as `'r'` for reading, `'w'` for writing, `'a'` for appending, `'r+'` for reading and writing, and `'b'` for binary mode .
- The `open()` function returns a file object, which can be used to work with files and directories.
- To read data from a file, we can use the `read()` method of the file object, which returns a string containing the entire content of the file .
- Alternatively, we can use the `readline()` method to read one line at a time, or the `readlines()` method to read all the lines and store them in a list .
- To write data to a file, we can use the `write()` method of the file object, which takes a string as an argument and writes it to the file .
- We can also use the `writelines()` method to write a list of strings to the file .
- To close a file, we can use the `close()` method of the file object, which frees up the resources associated with the file  .
- It is a good practice to use the `with` statement when working with files, as it automatically closes the file when the block of code is exited .
- To create a new file, we can use the `open()` function with the `'w'` mode, which will create the file if it does not exist, or overwrite it if it does .
- To delete a file, we can use the `os.remove()` function, which takes the file name as an argument and deletes it from the current working directory .
- To take input file from the terminal for a python script, we can use the `sys.argv` list, which contains the command-line arguments passed to the script.
- For example, if we run the script as `python script.py input.txt output.txt`, then `sys.argv[0]` will be `'script.py'`, `sys.argv[1]` will be `'input.txt'`, and `sys.argv[2]` will be `'output.txt'`.
- We can then use these arguments to open the input and output files and perform the desired operations.

# Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The Sieve of Eratosthenes is an algorithm to find all the prime numbers up to a given limit.
- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to the limit, and mark them all as true.
  - Starting from 2, the first prime number, iterate over the list and mark all the multiples of 2 as false, since they are not prime.
  - Find the next number in the list that is marked as true, and repeat the previous step, marking all its multiples as false.
  - Continue this process until the square of the current number is greater than the limit, as all the remaining numbers in the list are prime.
  - Return the list of numbers that are marked as true, as they are the prime numbers up to the limit.
- The algorithm can be implemented in Python as follows:

```python
def sieve_of_eratosthenes(limit):