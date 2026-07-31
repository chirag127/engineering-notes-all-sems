# File I/O : File input and output operations in Python Programming

## Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The Sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit n.
- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19 are prime numbers.
- The algorithm works by marking all the multiples of each prime number, starting from 2, as composite (not prime) in a boolean array of size n+1. The array is initialized with True values, except for 0 and 1 which are False.
- After the algorithm finishes, the array will contain True values only for the prime numbers less than or equal to n.
- The algorithm can be implemented in Python as follows:

```python
# Define a function to perform the sieve of Eratosthenes
def sieve_of_eratosthenes(n):
  # Create a boolean array of size n+1, initialized with True values
  is_prime = [True] * (n+1)
  # Mark 0 and 1 as False, as they are not prime
  is_prime[0] = is_prime[1] = False
  # Loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # If i is prime, mark all its multiples as False
    if is_prime[i]:
      for j in range(i*i, n+1, i):
        is_prime[j] = False
  # Return the list of prime numbers less than or equal to n
  return [i for i in range(n+1) if is_prime[i]]
```

- To test the function, we can print the prime numbers up to 100:

```python
# Print the prime numbers up to 100
print(sieve_of_eratosthenes(100))
```

- The output is:

```python
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

- The time complexity of the algorithm is O(n log log n), which is asymptotically faster than checking each number for primality individually. The space complexity is O(n), as we need to store the boolean array of size n+1.