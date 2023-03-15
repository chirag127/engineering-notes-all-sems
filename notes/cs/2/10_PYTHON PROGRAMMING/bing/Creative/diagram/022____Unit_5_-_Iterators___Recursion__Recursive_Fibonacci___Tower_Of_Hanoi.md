## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- A recursive function is a function that calls itself to solve smaller subproblems until a base case is reached. A base case is a simple case that can be solved directly without recursion.
- A recursive function to compute the nth Fibonacci number can be defined as follows:

```python
def fibonacci(n):
  # base case: the first and second Fibonacci numbers are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the nth Fibonacci number is the sum of the previous two
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

- The recursive function has two parameters: n, which is the position of the Fibonacci number to compute, and a memo, which is a dictionary that stores the previously computed Fibonacci numbers to avoid repeated calculations. The memo is initialized with the base cases: 1 and 1.
- The recursive function checks if n is in the memo. If yes, it returns the value stored in the memo. If not, it computes the nth Fibonacci number by calling itself with n-1 and n-2, and stores the result in the memo. Then it returns the result.

```python
def fibonacci(n, memo = {1: 1, 2: 1}):
  # check if n is in the memo
  if n in memo:
    return memo[n]
  # compute the nth Fibonacci number and store it in the memo
  else:
    result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = result
    return result
```

- The recursive function with memoization has a better time complexity than the recursive function without memoization, because it avoids repeated calculations. The time complexity of the recursive function without memoization is O(2^n), while the time complexity of the recursive function with memoization is O(n).

### Tower of Hanoi

- The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, making a conical shape.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.
- A recursive solution to the Tower of Hanoi puzzle can be defined as follows:

```python
def hanoi(n, source, target, auxiliary):
  # base case: if there is only one disk, move it from source to target
  if n == 1:
    print(f"Move disk 1 from {source} to {target}.")
    return
  # recursive case: move n-1 disks from source to auxiliary, using target as a temporary rod
  hanoi(n-1, source, auxiliary, target)
  # move the remaining disk from source to target
  print(f"Move disk {n} from {source} to {target}.")
  # move n-1 disks from auxiliary to target, using source as a temporary rod
  hanoi(n-1, auxiliary, target, source)
```

- The recursive function has four parameters: n, which is the number of disks to move, source, which is the rod where the disks are initially stacked, target, which is the rod where the disks are to be moved, and auxiliary, which is the rod that can be used as a temporary storage.
- The recursive function follows the following steps:
  - If there is only one disk, move it from source to target and return.
  - Otherwise, move n-1 disks from source to auxiliary, using target as a temporary rod. This can be done by calling the function recursively with n-1, source, auxiliary, and target as the parameters.
  - Move the remaining disk from source to target and print the move.
  - Move n-1 disks from auxiliary to target, using source as a temporary rod