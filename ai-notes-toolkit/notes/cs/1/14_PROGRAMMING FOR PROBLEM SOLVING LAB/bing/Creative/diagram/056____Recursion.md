## Recursion

Recursion is a technique of defining a problem in terms of itself. It is a way of solving problems that involves breaking them down into smaller and smaller subproblems until they are simple enough to be solved directly.

Some characteristics of recursion are:

- A recursive function calls itself with a smaller or simpler input.
- A recursive function has a base case that terminates the recursion when the input is trivial or invalid.
- A recursive function has a recursive case that reduces the input and calls itself again.
- A recursive function must converge to the base case, otherwise it will cause an infinite loop or a stack overflow.

Some examples of recursion are:

- Factorial: The factorial of a positive integer n is defined as n * (n-1) * (n-2) * ... * 1. The base case is when n is 1, and the recursive case is when n is greater than 1.
- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The base case is when n is 0 or 1, and the recursive case is when n is greater than 1.
- Binary Search: Binary search is a method of finding an element in a sorted array by repeatedly dividing the array into two halves and checking if the element is in the left or right half. The base case is when the array is empty or has one element, and the recursive case is when the array has more than one element.