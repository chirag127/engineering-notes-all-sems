# Recursively Defined Functions

A recursively defined function is a function that is defined in terms of itself, but with a smaller or simpler input. A recursively defined function consists of two parts: a base case and a recursive case.

- The base case specifies the value of the function for the smallest or simplest input, such as 0 or 1. For example, the base case of the factorial function n! is 0! = 1.
- The recursive case specifies the value of the function for a larger or more complex input in terms of the value of the function for a smaller or simpler input. For example, the recursive case of the factorial function n! is (n + 1)! = (n + 1) * n!.

A recursively defined function can be evaluated by repeatedly applying the recursive case until the base case is reached. For example, to evaluate 3!, we can use the recursive case to get:

3! = (3 + 1) * 3! = 4 * 3!
3! = 4 * (3 + 1) * 2! = 4 * 3 * 2!
3! = 4 * 3 * (2 + 1) * 1! = 4 * 3 * 2 * 1!
3! = 4 * 3 * 2 * 1 * 0! = 4 * 3 * 2 * 1 * 1 = 24

Recursively defined functions are useful for modeling problems that have a recursive structure, such as the Fibonacci sequence, the Towers of Hanoi, or the Ackermann function. Recursively defined functions can also be implemented in programming languages that support recursion, such as Python, Java, or C++. Recursion is a powerful technique that can simplify the code and reduce the time and space complexity of some algorithms. However, recursion also has some drawbacks, such as the risk of stack overflow, infinite recursion, or redundant computation. Therefore, it is important to use recursion carefully and wisely, and to compare it with other possible solutions, such as iteration or memoization.