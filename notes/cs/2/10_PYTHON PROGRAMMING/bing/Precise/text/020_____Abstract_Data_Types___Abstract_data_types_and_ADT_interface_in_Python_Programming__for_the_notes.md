### Abstract Data Types

An Abstract Data Type (ADT) is a high-level description of a collection of data and operations that can be performed on that data. It is an abstraction that defines a data type by its behavior, specifying the values and operations that can be performed on the data, but not the implementation of those operations.

In Python, an ADT can be implemented using classes. The class defines the data and the methods that operate on the data. The methods define the interface of the ADT, specifying the operations that can be performed on the data.

For example, a Stack ADT can be defined as a collection of elements with two main operations: push and pop. The push operation adds an element to the top of the stack, while the pop operation removes the top element from the stack.

Here is an example of a Stack ADT interface in Python:

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
```

### Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm for generating prime numbers. It was created by the Greek mathematician Eratosthenes. The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.

Here is an example of the Sieve of Eratosthenes algorithm in Python:

```python
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes
```

This function takes as input an integer `n` and returns a list of all prime numbers less than `n`. The function first creates a list of boolean values, representing whether each number is prime or not. It then iteratively marks the multiples of each prime number as not prime. Finally, it returns a list of all the prime numbers.