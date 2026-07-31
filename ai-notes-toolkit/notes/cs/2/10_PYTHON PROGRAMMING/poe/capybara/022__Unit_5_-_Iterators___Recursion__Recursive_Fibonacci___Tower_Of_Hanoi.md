## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

In this unit, we will learn about iterators and recursion, and how they can be used to solve problems. Specifically, we will focus on two classic problems: the Recursive Fibonacci sequence and the Tower of Hanoi puzzle.

### Iterators

An iterator is an object that allows us to traverse through a sequence of data. In Python, we can create an iterator using the `iter()` function. We can then use the `next()` function to iterate through each element of the sequence.

### Recursion

Recursion is a technique where a function calls itself to solve a problem. It is a powerful tool for solving problems that can be broken down into smaller, repetitive subproblems. However, it can also be a dangerous tool if not used correctly, as it can lead to infinite loops.

### Recursive Fibonacci

The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The sequence starts with 0 and 1, and continues as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

We can use recursion to compute the Fibonacci sequence. The base case for the recursion is when the input is 0 or 1, in which case we return the input. Otherwise, we recursively compute the Fibonacci number for the previous two numbers and add them together.

### Tower of Hanoi

The Tower of Hanoi is a classic problem that involves moving a stack of disks from one peg to another peg. The puzzle consists of three pegs and a number of disks of different sizes, which can be slid onto any peg. The objective of the puzzle is to move the entire stack to another peg, obeying the following simple rules:

- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
- No disk may be placed on top of a smaller disk.

We can use recursion to solve the Tower of Hanoi problem. The base case for the recursion is when there is only one disk, in which case we simply move it from the source peg to the destination peg. Otherwise, we recursively move the top n-1 disks from the source peg to the auxiliary peg, move the largest disk from the source peg to the destination peg, and then recursively move the n-1 disks from the auxiliary peg to the destination peg.

In conclusion, Iterators and Recursion are useful concepts in solving problems that involve sequences and repetitive subproblems. The Recursive Fibonacci sequence and the Tower of Hanoi puzzle are classic examples of problems that can be solved using these concepts.