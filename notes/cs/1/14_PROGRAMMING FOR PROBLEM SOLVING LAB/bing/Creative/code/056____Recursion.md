## Recursion

Recursion is a technique of defining a problem in terms of itself. It is a way of solving problems that involves breaking them down into smaller and simpler subproblems until they can be solved directly.

Some characteristics of recursion are:

- A recursive function calls itself with a smaller or simpler input.
- A recursive function has a base case that terminates the recursion when the input is trivial or cannot be reduced further.
- A recursive function has a recursive case that reduces the input and calls itself again.
- A recursive function must converge to the base case, otherwise it will result in an infinite loop or a stack overflow.

Some examples of recursion are:

- Factorial: The factorial of a positive integer n is defined as n! = n * (n-1) * (n-2) * ... * 1. The base case is n = 0 or n = 1, where n! = 1. The recursive case is n! = n * (n-1)!, where the input is reduced by 1.
- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The base case is n = 0 or n = 1, where F(n) = n. The recursive case is F(n) = F(n-1) + F(n-2), where the input is reduced by 2.
- Binary search: Binary search is a method of finding an element in a sorted array by repeatedly dividing the array into two halves and checking if the element is in the left or right half. The base case is when the array is empty or has one element, where the element is either found or not found. The recursive case is when the array has more than one element, where the input is reduced by half.