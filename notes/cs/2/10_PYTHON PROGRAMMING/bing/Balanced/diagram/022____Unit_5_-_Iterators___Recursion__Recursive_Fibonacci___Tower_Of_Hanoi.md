## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- A recursive function is a function that calls itself to solve smaller subproblems until a base case is reached. A base case is a simple case that can be solved directly without recursion.
- A recursive function to compute the nth Fibonacci number can be defined as follows:

```python
def fib(n):
  # base case: the first and second Fibonacci numbers are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the nth Fibonacci number is the sum of the previous two
  else:
    return fib(n-1) + fib(n-2)
```

- The recursive function has two parameters: n, which is the position of the Fibonacci number to compute, and a return value, which is the Fibonacci number at that position.
- The recursive function has two branches: one for the base case and one for the recursive case.
- The base case checks if n is 1 or 2, and returns 1 in either case. This is because the first and second Fibonacci numbers are both 1.
- The recursive case calls the function itself twice, with n-1 and n-2 as arguments, and adds the results. This is because the nth Fibonacci number is the sum of the previous two Fibonacci numbers.
- The recursive function terminates when the base case is reached, and returns the final result to the original caller.

### Tower of Hanoi

- The Tower of Hanoi is a classic puzzle that involves moving a stack of disks from one peg to another, following some rules. The rules are:
  - There are three pegs: A, B, and C.
  - The disks are of different sizes and are initially stacked on peg A in decreasing order of size, with the largest disk at the bottom and the smallest disk at the top.
  - Only one disk can be moved at a time.
  - A disk can only be moved to an empty peg or on top of a larger disk.
  - The goal is to move all the disks from peg A to peg C, using peg B as an auxiliary peg.
- A recursive function to solve the Tower of Hanoi puzzle can be defined as follows:

```python
def hanoi(n, source, target, auxiliary):
  # base case: there is only one disk to move
  if n == 1:
    print(f"Move disk 1 from {source} to {target}.")
  # recursive case: there are more than one disks to move
  else:
    # move the top n-1 disks from source to auxiliary, using target as an auxiliary
    hanoi(n-1, source, auxiliary, target)
    # move the bottom disk from source to target
    print(f"Move disk {n} from {source} to {target}.")
    # move the n-1 disks from auxiliary to target, using source as an auxiliary
    hanoi(n-1, auxiliary, target, source)
```

- The recursive function has four parameters: n, which is the number of disks to move, source, which is the peg where the disks are initially, target, which is the peg where the disks should end up, and auxiliary, which is the peg that can be used as a helper.
- The recursive function has two branches: one for the base case and one for the recursive case.
- The base case checks if n is 1, and prints a message to move the disk from source to target. This is because there is only one disk to move and it can be moved directly.
- The recursive case calls the function itself three times, with different arguments, and prints a message to move the bottom disk from source to target. This is because there are more than one disks to move and they can be moved in three steps:
  - Move the top n-1 disks from source to auxiliary, using target as an auxiliary. This is a smaller subproblem of the same kind, and can be solved recursively.
  - Move the bottom disk from source to target. This is the base case, and can be solved directly.
  - Move the n-1 disks from auxiliary to target, using source as an auxiliary. This is another smaller subproblem of the same kind, and can be solved recursively.
- The recursive