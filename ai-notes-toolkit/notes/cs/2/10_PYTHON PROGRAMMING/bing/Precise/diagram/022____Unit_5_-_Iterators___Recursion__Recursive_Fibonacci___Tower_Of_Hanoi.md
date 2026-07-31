## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc. The Fibonacci sequence can be defined recursively as follows:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

A recursive function to calculate the nth Fibonacci number can be written as follows:
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### Tower of Hanoi
The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
- No disk may be placed on top of a smaller disk.

A recursive solution to the Tower of Hanoi puzzle can be written as follows:
```python
def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        print(f'Move disk {n} from {source} to {target}')
        hanoi(n-1, auxiliary, target, source)
```
This function takes as input the number of disks `n`, the source rod, the target rod, and an auxiliary rod. It prints the sequence of moves required to solve the puzzle.