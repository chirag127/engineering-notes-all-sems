## Recursion

Recursion is a technique of defining a problem in terms of itself. It is a way of solving complex problems by breaking them down into smaller and simpler subproblems that have the same structure as the original problem.

Recursion involves two main components:

- A **base case** or **terminating condition** that defines the simplest version of the problem and provides a direct solution.
- A **recursive step** or **recursive call** that reduces the problem to a smaller and simpler subproblem, and then calls itself with the new subproblem as the input.

Recursion can be used to implement algorithms that are naturally recursive, such as:

- Factorial: The factorial of a positive integer n is defined as n! = n * (n-1) * (n-2) * ... * 1. The base case is n = 1, where n! = 1. The recursive step is n! = n * (n-1)!, where the problem is reduced by one.
- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. The base case is n = 1 or n = 2, where the nth Fibonacci number is 1. The recursive step is F(n) = F(n-1) + F(n-2), where the problem is reduced by two.
- Binary Search: Binary search is an algorithm that finds the position of a target value within a sorted array. The base case is when the array has one element, where the position is either found or not. The recursive step is to compare the target value with the middle element of the array, and then call itself with the half of the array that contains the target value, where the problem is reduced by half.

Recursion has some advantages and disadvantages over iterative solutions, such as:

- Advantages: Recursion can make the code more concise, elegant, and easy to understand. Recursion can also handle problems that have variable or unknown depth, such as tree traversal, backtracking, and dynamic programming.
- Disadvantages: Recursion can consume more memory and time, as each recursive call creates a new stack frame that stores the local variables and parameters. Recursion can also cause stack overflow, which is an error that occurs when the stack size exceeds the limit. Recursion can also be harder to debug and trace.