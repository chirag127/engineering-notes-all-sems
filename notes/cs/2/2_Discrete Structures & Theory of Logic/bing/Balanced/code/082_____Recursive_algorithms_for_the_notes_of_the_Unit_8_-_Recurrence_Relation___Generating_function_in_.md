# Recursive algorithms

A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem. A recursive algorithm must have a base case, which is a condition that terminates the recursion, and a recursive step, which is a rule that reduces the problem size and makes a recursive call.

## Examples of recursive algorithms

Some examples of problems that can be solved easily by recursive algorithms are:

- Factorial: The factorial of a positive integer n is defined as n! = n * (n-1) * (n-2) * ... * 1. The base case is n = 0, which has a factorial of 1. The recursive step is n! = n * (n-1)!, which reduces the problem size by 1 and makes a recursive call.
- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. The base case is n = 1 or n = 2, which have Fibonacci values of 1. The recursive step is F(n) = F(n-1) + F(n-2), which reduces the problem size by 2 and makes two recursive calls.
- Merge sort: Merge sort is a sorting algorithm that divides an array into two halves, recursively sorts each half, and then merges the two sorted halves. The base case is an array of size 0 or 1, which is already sorted. The recursive step is to split the array into two halves, recursively sort each half, and then merge the two sorted halves using a helper function.
- Tower of Hanoi: The Tower of Hanoi is a puzzle where there are three pegs and n disks of different sizes stacked on one peg. The goal is to move all the disks to another peg, following these rules: only one disk can be moved at a time, a disk can only be moved to an empty peg or on top of a larger disk, and no disk can be placed on top of a smaller disk. The base case is n = 0, which means there are no disks to move. The recursive step is to move n-1 disks from the source peg to the auxiliary peg, then move the largest disk from the source peg to the destination peg, and then move n-1 disks from the auxiliary peg to the destination peg.

## Properties of recursive algorithms

Some properties of recursive algorithms are:

- They are often simpler and more elegant than iterative algorithms, as they express the problem in terms of itself.
- They may use more memory and time than iterative algorithms, as they need to store the state of each recursive call in the call stack and make multiple function calls.
- They may cause stack overflow errors if the recursion depth is too large or the base case is not reached.
- They may need to handle edge cases or invalid inputs carefully, as they may cause infinite recursion or incorrect results.