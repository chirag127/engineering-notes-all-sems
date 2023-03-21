## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

In this unit, we will cover two important concepts in programming - Iterators and Recursion. We will learn how to use these concepts to solve two classic problems: Recursive Fibonacci and Tower of Hanoi.

### Iterators

An iterator is an object that represents a stream of data. It allows us to traverse a collection of data, one item at a time, without having to know the underlying data structure. In Python, iterators are implemented as classes that define two methods: `__iter__` and `__next__`.

- The `__iter__` method returns the iterator object itself.
- The `__next__` method returns the next item in the collection. If there are no more items, it raises the `StopIteration` exception.

We can use the `for` loop to iterate over an iterator. Here's an example:

```python
my_list = [1, 2, 3]
my_iterator = iter(my_list)

for item in my_iterator:
    print(item)
```

This will output:

```
1
2
3
```

### Recursion

Recursion is a powerful technique in programming where a function calls itself to solve a problem. Recursion can be used to solve many problems that are difficult or impossible to solve iteratively. However, recursion can also be dangerous if not used correctly, as it can lead to infinite loops.

Here's an example of a recursive function to calculate the nth Fibonacci number:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

This function uses recursion to calculate the nth Fibonacci number by adding the two previous Fibonacci numbers. The base case is when `n` is less than or equal to 1, in which case the function returns `n`.

### Recursive Fibonacci

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers in the series are 0 and 1. Here's an example sequence:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

We can use recursion to calculate the nth number in the Fibonacci sequence. Here's an example implementation:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### Tower of Hanoi

The Tower of Hanoi is a classic puzzle where we are given three pegs and a set of disks of different sizes. The disks are initially stacked on one peg in order of size, with the largest at the bottom and the smallest at the top. The goal is to move the entire stack to another peg, while obeying the following rules:

- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or an empty peg.
- No disk may be placed on top of a smaller disk.

We can solve the Tower of Hanoi puzzle using recursion. Here's an example implementation:

```python
def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(f"Move disk 1 from peg {from_peg} to peg {to_peg}")
        return
    tower_of_hanoi(n-1, from_peg, aux_peg, to_peg)
    print(f"Move disk {n} from peg {from_peg} to peg {to_peg}")
    tower_of_hanoi(n-1, aux_peg, to_peg, from_peg)
```

This function takes in the number of disks `n` and the three pegs. It uses recursion to move the disks from the first peg to the second peg, using the third peg as an auxiliary peg. The base case is when there is only one disk, in which case the function simply moves the disk from the first peg to the second peg.