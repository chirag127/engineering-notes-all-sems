## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.

A recursive function is a function that calls itself. The Fibonacci sequence can be calculated using a recursive function. Here is an example of a recursive function that calculates the nth Fibonacci number:

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### Tower of Hanoi

The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

Here is an example of a recursive function that solves the Tower of Hanoi puzzle:

```python
def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n-1, source, target, auxiliary)
        print(f'Move disk {n} from {source} to {target}')
        hanoi(n-1, auxiliary, source, target)
```

This function takes four arguments: the number of disks `n`, the source rod, the auxiliary rod, and the target rod. It moves the `n` disks from the source rod to the target rod using the auxiliary rod. The function calls itself recursively to move the `n-1` smaller disks from the source rod to the auxiliary rod, then moves the largest disk from the source rod to the target rod, and finally moves the `n-1` smaller disks from the auxiliary rod to the target rod. The function prints the moves it makes.