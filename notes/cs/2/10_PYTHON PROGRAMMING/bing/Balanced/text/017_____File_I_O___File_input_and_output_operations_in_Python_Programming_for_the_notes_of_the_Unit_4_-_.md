### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- Python provides built-in functions and modules to handle various types of files, such as text files, binary files, CSV files, JSON files, etc.
- To perform file I/O operations in Python, we need to follow these steps:
  - Open the file using the `open()` function, which returns a file object.
  - Perform the desired read or write operations on the file object using methods such as `read()`, `write()`, `readline()`, `writelines()`, etc.
  - Close the file using the `close()` method of the file object, or use the `with` statement to automatically close the file when the block ends.
- The `open()` function takes two parameters: the file name and the mode. The mode specifies how the file is opened, such as `'r'` for reading, `'w'` for writing, `'a'` for appending, `'b'` for binary mode, etc.
- The file object has various attributes and methods to access and manipulate the file data, such as `name`, `mode`, `closed`, `seek()`, `tell()`, `flush()`, etc.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The Sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit n.
- The algorithm works by creating a list of numbers from 2 to n, and marking the multiples of each prime number as composite, starting from 2. The remaining unmarked numbers are prime.
- The steps of the algorithm are as follows:
  - Create a boolean array of size n+1, and initialize all the elements to True, except for 0 and 1, which are False.
  - Loop from 2 to the square root of n, and for each number i, check if it is True in the array.
  - If i is True, it means it is a prime number, so loop from i*i to n, and mark every multiple of i as False in the array, using a step size of i.
  - After the loop ends, the array will contain True for the prime numbers and False for the composite numbers.
  - Return the list of indices of the array that are True, which are the prime numbers up to n.
- The following is a Python implementation of the Sieve of Eratosthenes algorithm:

```python
def sieve_of_eratosthenes(n):
  # create a boolean array of size n+1
  is_prime = [True] * (n+1)
  # mark 0 and 1 as False
  is_prime[0] = is_prime[1] = False
  # loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # check if i is True in the array
    if is_prime[i]:
      # mark every multiple of i as False in the array
      for j in range(i*i, n+1, i):
        is_prime[j] = False
  # return the list of indices that are True, which are the prime numbers
  return [i for i in range(n+1) if is_prime[i]]
```