## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

- In this unit, we will learn about two important concepts in computer science: iterators and recursion.
- Iterators are objects that allow us to traverse through a collection of elements, such as a list, a string, or a file, in a sequential and uniform way.
- Recursion is a technique of defining a problem in terms of smaller instances of the same problem, and using a base case to stop the recursion.
- We will see how iterators and recursion can be used to implement some common algorithms, such as the Fibonacci sequence and the Tower of Hanoi puzzle.

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers that starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. For example, the first 10 numbers of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
- The Fibonacci sequence can be defined recursively as follows:

  - F(0) = 0
  - F(1) = 1
  - F(n) = F(n-1) + F(n-2) for n > 1

- This means that to find the nth Fibonacci number, we need to find the (n-1)th and the (n-2)th Fibonacci numbers, and add them together. This process repeats until we reach the base cases of F(0) and F(1), which are known values.
- We can implement the recursive Fibonacci algorithm in Python as follows:

```python
def fibonacci(n):
  # base cases
  if n == 0:
    return 0
  if n == 1:
    return 1
  # recursive case
  return fibonacci(n-1) + fibonacci(n-2)
```

- The recursive Fibonacci algorithm has a time complexity of O(2^n), which means that it is very inefficient for large values of n. This is because it performs a lot of redundant calculations, such as computing F(n-2) twice for each call to F(n).
- To improve the efficiency of the recursive Fibonacci algorithm, we can use a technique called memoization, which is a way of storing the results of previous computations in a dictionary or a list, and looking them up instead of recomputing them. For example, we can modify the recursive Fibonacci algorithm as follows:

```python
# create a global dictionary to store the results
memo = {}

def fibonacci(n):
  # base cases
  if n == 0:
    return 0
  if n == 1:
    return 1
  # check if the result is already in the memo
  if n in memo:
    return memo[n]
  # otherwise, compute the result and store it in the memo
  result = fibonacci(n-1) + fibonacci(n-2)
  memo[n] = result
  return result
```

- The memoized Fibonacci algorithm has a time complexity of O(n), which means that it is much more efficient than the original recursive Fibonacci algorithm. This is because it avoids recomputing the same values over and over again, and only performs one addition for each call to F(n).

### Tower of Hanoi

- The Tower of Hanoi is a classic puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, making a conical shape.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.

- The Tower of Hanoi puzzle can be solved recursively as follows:

  - To move n disks from rod A to rod C, using rod B as an auxiliary rod, we need to:
    - Move n-1 disks from rod A to rod B, using rod C as an auxiliary rod.
    - Move the largest disk from rod A to rod C.
    - Move n-1 disks from rod B to rod C, using rod A as an auxiliary rod.
  - The base case is when n is 1, in which case we simply move the disk from rod A to rod C.

- We can implement the recursive Tower of Hanoi algorithm in Python as follows:

```python
def hanoi(n

```
