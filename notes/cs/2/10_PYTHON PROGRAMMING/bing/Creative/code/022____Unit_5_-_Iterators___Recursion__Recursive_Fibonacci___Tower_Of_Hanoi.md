Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn. Here is the content for Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi.

# Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

## Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- A recursive function is a function that calls itself to solve smaller subproblems until a base case is reached. A base case is a simple case that can be solved directly without recursion.
- A recursive function for the Fibonacci sequence can be defined as follows:

```python
def fibonacci(n):
  # base case: the first and second numbers are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the nth number is the sum of the previous two numbers
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

- The recursive function works by breaking down the problem into smaller subproblems. For example, to find the 5th Fibonacci number, we can use the following steps:

```python
fibonacci(5) = fibonacci(4) + fibonacci(3) # recursive case
fibonacci(4) = fibonacci(3) + fibonacci(2) # recursive case
fibonacci(3) = fibonacci(2) + fibonacci(1) # recursive case
fibonacci(2) = 1 # base case
fibonacci(1) = 1 # base case
```

- The recursive function returns the value of the base case when it is reached, and then adds up the values from the smaller subproblems. For example, to find the 5th Fibonacci number, we can use the following steps:

```python
fibonacci(5) = fibonacci(4) + fibonacci(3) # recursive case
fibonacci(4) = fibonacci(3) + fibonacci(2) # recursive case
fibonacci(3) = fibonacci(2) + fibonacci(1) # recursive case
fibonacci(2) = 1 # base case
fibonacci(1) = 1 # base case
fibonacci(5) = (1 + 1) + (1 + 1) # add up the values from the base cases
fibonacci(5) = 2 + 2 # simplify
fibonacci(5) = 4 # final answer
```

## Tower Of Hanoi

- The Tower of Hanoi is a classic puzzle game that involves moving a stack of disks from one peg to another, following some rules. The rules are:
  - Only one disk can be moved at a time.
  - A disk can only be moved if it is the topmost disk on a peg.
  - A disk can only be placed on a peg if it is smaller than the disk below it or if the peg is empty.
- The goal is to move all the disks from the first peg to the last peg, using the middle peg as an auxiliary.
- A recursive function for the Tower of Hanoi can be defined as follows:

```python
def hanoi(n, source, aux, target):
  # base case: if there are no disks to move, do nothing
  if n == 0:
    return
  # recursive case: move n-1 disks from source to aux, using target as an auxiliary
  hanoi(n-1, source, target, aux)
  # move the nth disk from source to target
  print(f"Move disk {n} from {source} to {target}")
  # move n-1 disks from aux to target, using source as an auxiliary
  hanoi(n-1, aux, source, target)
```

- The recursive function works by breaking down the problem into smaller subproblems. For example, to move 3 disks from peg A to peg C, using peg B as an auxiliary, we can use the following steps:

```python
hanoi(3, A, B, C) # move 3 disks from A to C, using B as an auxiliary
hanoi(2, A, C, B) # move 2 disks from A to B, using C as an auxiliary
hanoi(1, A, B, C) # move 1 disk from A to C, using B as an auxiliary