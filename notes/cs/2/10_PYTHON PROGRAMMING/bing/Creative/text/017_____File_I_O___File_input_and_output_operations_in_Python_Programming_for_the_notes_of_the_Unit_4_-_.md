### File I/O : File input and output operations in Python Programming

- File input and output in python is to get input in a program from a file and write output to the same or another file.
- Python provides some built-in functions to perform both input and output operations, such as `print()`, `input()`, `open()`, `read()`, `write()`, and `close()`.
- To open a file in python, we use the `open()` function, which takes two arguments: the file name and the mode. The mode can be `'r'` for reading, `'w'` for writing, `'a'` for appending, or `'r+'` for both reading and writing .
- To read data from a file, we use the `read()` method of the file object, which returns a string containing the entire content of the file. We can also use the `readline()` method to read one line at a time, or the `readlines()` method to read all the lines into a list .
- To write data to a file, we use the `write()` method of the file object, which takes a string as an argument and writes it to the file. We can also use the `writelines()` method to write a list of strings to the file .
- To close a file, we use the `close()` method of the file object, which frees up the resources associated with the file. It is a good practice to close the file after we are done with it .
- To create a new file, we can use the `'w'` mode in the `open()` function, which will create the file if it does not exist, or overwrite it if it does. To delete a file, we can use the `remove()` function from the `os` module, which takes the file name as an argument and deletes it from the disk .
- To take input file from the terminal for python script, we can use the `sys` module, which provides access to the command-line arguments. The `sys.argv` is a list that contains the script name and the arguments passed to it. We can assign the input and output file names to variables using the `sys.argv` list.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The sieve of Eratosthenes is an algorithm that finds all the prime numbers up to a given limit. A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to the limit, and mark them all as true.
  - Start from the smallest number 2, and mark all its multiples (except itself) as false, since they are not prime.
  - Find the next number that is still marked as true, and repeat the previous step for it, marking all its multiples as false.
  - Continue this process until we reach the square root of the limit, or there are no more numbers marked as true.
  - The numbers that are still marked as true are the prime numbers up to the limit.
- The following is an example of python code that implements the sieve of Eratosthenes algorithm:

```python
# define the limit
limit = 100

# create a list of booleans from 2 to limit
is_prime = [True] * (limit + 1)

# loop from 2 to the square root of limit
for i in range(2, int(limit**0.5) + 1):
  # if i is marked as prime
  if is_prime[i]:
    # mark all the multiples of i as not prime
    for j in range(i * i, limit + 1, i):
      is_prime[j] = False

# print the prime numbers
for i in range(2, limit + 1):
  if is_prime[i]:
    print(i, end=" ")
```