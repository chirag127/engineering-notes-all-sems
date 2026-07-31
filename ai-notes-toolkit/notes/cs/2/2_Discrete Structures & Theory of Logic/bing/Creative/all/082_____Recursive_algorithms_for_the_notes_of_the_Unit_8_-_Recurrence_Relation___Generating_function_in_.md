# Recursive algorithms

A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem. A recursive algorithm must have a base case, which is a condition that terminates the recursion, and a recursive step, which is a rule that reduces the problem size and makes a recursive call.

## Examples of recursive algorithms

Some examples of problems that can be solved easily by recursive algorithms are:

- Factorial: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. The factorial of 0 is defined to be 1. A recursive algorithm to compute n! is:

```
factorial(n):
  if n == 0 or n == 1: # base case
    return 1
  else: # recursive step
    return n * factorial(n - 1)
```

- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. For example, the first 10 Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. A recursive algorithm to compute the nth Fibonacci number is:

```
fibonacci(n):
  if n == 0 or n == 1: # base case
    return n
  else: # recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)
```

- Merge sort: Merge sort is a sorting algorithm that divides an array into two halves, recursively sorts each half, and then merges the two sorted halves. A recursive algorithm to perform merge sort is:

```
merge_sort(array):
  if len(array) <= 1: # base case
    return array
  else: # recursive step
    mid = len(array) // 2
    left = merge_sort(array[:mid]) # sort left half
    right = merge_sort(array[mid:]) # sort right half
    return merge(left, right) # merge the two sorted halves
```

- Tower of Hanoi: The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.

A recursive algorithm to solve the Tower of Hanoi puzzle is:

```
tower_of_hanoi(n, source, destination, auxiliary):
  if n == 1: # base case
    print("Move disk 1 from rod", source, "to rod", destination)
    return
  else: # recursive step
    tower_of_hanoi(n - 1, source, auxiliary, destination) # move n - 1 disks from source to auxiliary
    print("Move disk", n, "from rod", source, "to rod", destination) # move the largest disk from source to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source) # move n - 1 disks from auxiliary to destination
```

## Advantages and disadvantages of recursive algorithms

Some advantages of recursive algorithms are:

- They are simple and elegant, and can reduce the complexity of the code.
- They can handle dynamic data structures such as trees and graphs easily.
- They can express some mathematical concepts and patterns naturally.

Some disadvantages of recursive algorithms are:

- They may cause stack overflow, which is an error that occurs when the call stack exceeds its limit due to too many recursive calls.
- They may have a high time and space complexity, which means they can be slower and consume more memory than iterative algorithms.
- They may be difficult to debug and understand, especially for complex problems.