### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- A file is a collection of data stored in a disk or other storage device with a name and a path.
- Python provides built-in functions and modules to perform file I/O operations such as open, read, write, close, etc.
- To perform file I/O operations, we need to follow these steps:
  - Open a file using the open function, which returns a file object.
  - Perform the desired operation on the file object, such as reading or writing data, using methods such as read, write, readline, writelines, etc.
  - Close the file using the close method of the file object, which frees the resources associated with the file.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- The Sieve of Eratosthenes is an algorithm to find all the prime numbers up to a given limit n.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to n, and mark them all as true.
  - Starting from 2, the first prime number, iterate over the list and mark all the multiples of 2 as false, since they are not prime.
  - Find the next number in the list that is marked as true, and repeat the previous step, marking all the multiples of that number as false.
  - Continue this process until the square of the current number is greater than n, since all the remaining numbers in the list are prime.
  - Return the list of numbers that are marked as true, which are the prime numbers up to n.

- Here is an example of the Sieve of Eratosthenes algorithm in Python:

```python
# Define a function to implement the Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
  # Create a list of consecutive integers from 2 to n, and mark them all as true
  prime = [True for i in range(n + 1)]
  # Initialize the current number as 2, the first prime number
  p = 2
  # Loop until the square of the current number is greater than n
  while p * p <= n:
    # If the current number is marked as true, it is prime
    if prime[p]:
      # Mark all the multiples of the current number as false, since they are not prime
      for i in range(p * p, n + 1, p):
        prime[i] = False
    # Increment the current number by 1
    p += 1
  # Return the list of numbers that are marked as true, which are the prime numbers up to n
  return [i for i in range(2, n + 1) if prime[i]]

# Test the function with an example
n = 20
print(f"The prime numbers up to {n} are:")
print(sieve_of_eratosthenes(n))
```

- The output of the above code is:

```
The prime numbers up to 20 are:
[2, 3, 5, 7, 11, 13, 17, 19]
```