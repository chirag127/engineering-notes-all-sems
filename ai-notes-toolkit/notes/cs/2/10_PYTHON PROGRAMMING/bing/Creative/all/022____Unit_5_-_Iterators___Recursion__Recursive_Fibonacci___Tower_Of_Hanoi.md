## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- A recursive function is a function that calls itself to solve smaller subproblems until a base case is reached. A base case is a simple case that can be solved directly without recursion.
- A recursive function to compute the nth Fibonacci number can be defined as follows:

```python
def fib(n):
  # base case: n is 0 or 1
  if n == 0 or n == 1:
    return n
  # recursive case: n is greater than 1
  else:
    return fib(n-1) + fib(n-2)
```

- The function fib(n) returns the nth Fibonacci number by adding the (n-1)th and the (n-2)th Fibonacci numbers, which are computed by calling fib(n-1) and fib(n-2) recursively. The base case is when n is 0 or 1, in which case the function returns n itself.
- The recursive Fibonacci function has a time complexity of O(2^n), which means it grows exponentially with the input size. This is because each recursive call makes two more recursive calls, resulting in a binary tree of calls that doubles at each level. The space complexity is also O(2^n), as each recursive call requires its own stack frame.

### Tower of Hanoi

- The Tower of Hanoi is a classic puzzle that involves moving a stack of disks from one peg to another, following some rules. The rules are:
  - Only one disk can be moved at a time.
  - A disk can only be moved if it is the topmost disk on a peg.
  - A disk can only be placed on a larger disk or an empty peg.
- The puzzle can be solved recursively by breaking it down into smaller subproblems. The general algorithm is as follows:

```python
def hanoi(n, source, target, auxiliary):
  # base case: n is 0
  if n == 0:
    return
  # recursive case: n is greater than 0
  else:
    # move n-1 disks from source to auxiliary, using target as a temporary peg
    hanoi(n-1, source, auxiliary, target)
    # move the largest disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # move n-1 disks from auxiliary to target, using source as a temporary peg
    hanoi(n-1, auxiliary, target, source)
```

- The function hanoi(n, source, target, auxiliary) moves n disks from the source peg to the target peg, using the auxiliary peg as a temporary storage. The base case is when n is 0, in which case nothing needs to be moved. The recursive case is when n is greater than 0, in which case the function does the following steps:
  - Move n-1 disks from the source peg to the auxiliary peg, using the target peg as a temporary storage. This can be done by calling hanoi(n-1, source, auxiliary, target) recursively.
  - Move the largest disk from the source peg to the target peg. This can be done by printing a message indicating the move.
  - Move n-1 disks from the auxiliary peg to the target peg, using the source peg as a temporary storage. This can be done by calling hanoi(n-1, auxiliary, target, source) recursively.
- The recursive Tower of Hanoi function has a time complexity of O(2^n), which means it grows exponentially with the input size. This is because each recursive call makes two more recursive calls, resulting in a binary tree of calls that doubles at each level. The space complexity is also O(2^n), as each recursive call requires its own stack frame.