## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

- In this unit, we will learn about two important concepts in computer science: iterators and recursion.
- Iterators are objects that allow us to traverse through a collection of elements, such as a list, a string, or a file, in a sequential and uniform way.
- Recursion is a technique of defining a problem in terms of smaller instances of the same problem, and solving it by using a base case and a recursive step.
- We will see how these concepts can be applied to solve some classic problems, such as the Fibonacci sequence and the Tower of Hanoi puzzle.

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers that starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. For example, the first 10 numbers of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
- We can define the Fibonacci sequence recursively as follows:

  - Base case: F(0) = 0, F(1) = 1
  - Recursive step: F(n) = F(n-1) + F(n-2) for n > 1

- This means that to find the nth Fibonacci number, we need to find the (n-1)th and the (n-2)th Fibonacci numbers, and add them together. We can implement this definition in Python using a recursive function:

```python
def fibonacci(n):
  # base case
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # recursive step
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

- This function will return the nth Fibonacci number for any non-negative integer n. For example, fibonacci(5) will return 5, and fibonacci(10) will return 34.
- However, this function is not very efficient, because it repeats a lot of calculations. For example, to find fibonacci(5), we need to find fibonacci(4) and fibonacci(3), but to find fibonacci(4), we also need to find fibonacci(3) and fibonacci(2), and so on. This leads to an exponential growth in the number of function calls, which can slow down the program significantly.
- A better way to implement the Fibonacci sequence is to use an iterative approach, where we use a loop to keep track of the previous two Fibonacci numbers, and update them as we go along. For example, we can use a while loop to implement the Fibonacci sequence in Python:

```python
def fibonacci(n):
  # initialize the first two Fibonacci numbers
  a = 0
  b = 1
  # loop until we reach the nth Fibonacci number
  while n > 0:
    # update the next Fibonacci number as the sum of the previous two
    c = a + b
    # update the previous two Fibonacci numbers
    a = b
    b = c
    # decrement n by 1
    n -= 1
  # return the last Fibonacci number
  return a
```

- This function will also return the nth Fibonacci number for any non-negative integer n, but it will do so much faster, because it does not repeat any calculations. For example, fibonacci(5) will return 5, and fibonacci(10) will return 34, but it will only use one loop iteration for each n, instead of many recursive calls.

### Tower of Hanoi

- The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks stacked on one rod in order of decreasing size, such that the smallest disk is on top and the largest disk is on the bottom. The objective of the puzzle is to move the entire stack of disks from the first rod to the last rod, following these rules:

  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the rods and sliding it onto another rod, on top of the other disks that may already be present on that rod.
  - No disk may be placed on top of a smaller disk.

- For example, if we have three disks, labeled A, B, and C, from smallest to largest, and three rods, labeled 1, 2, and 3, from left to right, the puzzle starts with the disks stacked on rod 1 as follows:

```
  A
  B
  C