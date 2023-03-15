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

- The recursive function has two main parts: the base case and the recursive case. The base case handles the simplest cases, where n is 1 or 2. The recursive case handles the general cases, where n is larger than 2. The recursive case calls the function itself with smaller arguments, until the base case is reached.
- The recursive function can be visualized as a tree of function calls, where each node represents a call to the function with a certain argument. The leaves of the tree are the base cases, and the root of the tree is the original call. For example, the tree for fibonacci(5) is:

```
fibonacci(5)
   /      \
fibonacci(4) fibonacci(3)
 /     \      /     \
fibonacci(3) fibonacci(2) fibonacci(2) fibonacci(1)
 /     \
fibonacci(2) fibonacci(1)
```

- The value of each node is the return value of the function call. The value of the root node is the final answer. To compute the value of each node, we need to compute the value of its children first. For example, to compute fibonacci(5), we need to compute fibonacci(4) and fibonacci(3) first, and then add them together. To compute fibonacci(4), we need to compute fibonacci(3) and fibonacci(2) first, and so on. This process is called recursion, and it follows the structure of the function definition.

### Tower of Hanoi

- The Tower of Hanoi is a classic puzzle game that involves moving a stack of disks from one peg to another, following some rules. The rules are:

  - Only one disk can be moved at a time.
  - A disk can only be moved if it is the topmost disk on a peg.
  - A disk can only be placed on a larger disk or an empty peg.

- The goal is to move all the disks from the first peg to the last peg, using the middle peg as an auxiliary. For example, the initial state and the goal state of the puzzle with three disks are:

```
Initial state:    Goal state:

   |              |              |                |              |              |
  ===             |              |               ===             |              |
 =====            |              |              =====            |              |
=======           |              |             =======           |              |
-------      -------      -------           -------      -------      -------
  A            B            C                A            B            C
```

- A recursive function to solve the Tower of Hanoi puzzle can be defined as follows:

```python
def hanoi(n, source, aux, target):
  # base case: if there are no disks to move, do nothing
  if n == 0:
    return
  # recursive case: move n-1 disks from source to aux, using target as an auxiliary
  hanoi(n-1, source, target, aux)
  # move the largest disk from source to target
  print(f"Move disk {n} from {source} to {target}")
  # move n-1 disks from aux to target, using source as an auxiliary
  hanoi(n-1, aux, source, target)
```

- The recursive function has two main parts: the base case and the recursive case. The base case handles the simplest case, where there are no disks to move. The recursive case handles the general case, where there are n disks to move. The recursive case has three steps:

  - Move the top n-1 disks from the source peg to the auxiliary peg, using the target peg as an auxiliary. This