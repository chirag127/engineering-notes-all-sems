## Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi

### Recursive Fibonacci
- The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers.
- The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.
- The recursive function to generate the nth Fibonacci number is defined as follows:
    - If n is 0, return 0
    - If n is 1, return 1
    - Otherwise, return the sum of the (n-1)th and (n-2)th Fibonacci numbers
- Here is an example of a recursive function to generate the nth Fibonacci number in Python:
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### Tower Of Hanoi
- The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod.
- The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
    - Only one disk can be moved at a time.
    - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    - No disk may be placed on top of a smaller disk.
- The minimum number of moves required to solve a Tower of Hanoi puzzle is 2^n - 1, where n is the number of disks.
- Here is an example of a recursive function to solve the Tower of Hanoi puzzle in Python:
```python
def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        print(f'Move disk {n} from {source} to {target}')
        hanoi(n-1, auxiliary, target, source)
```