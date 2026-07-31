 Here is the formal notes on Recursive definition of functions for the notes of the Unit 8 - Recurrence Relation & Generating function in the subject of Discrete Structures & Theory of Logic:

### Recursive definition of functions

 A function f is said to be recursively defined if its definition involves the function itself. In other words, the function is defined in terms of its own previous values.

A few examples of recursively defined functions are:

1. Function to calculate factorial of a number n:
f(n) = n * f(n-1)      // Base case: f(0) = 1

2. Function to calculate sum of first n natural numbers:
f(n) = n + f(n-1)      // Base case: f(1) = 1

3. Function to calculate Fibonacci number at position n:
f(n) = f(n-1) + f(n-2)   // Base cases: f(0) = 0, f(1) = 1

Recursive definitions allow us to define functions for which a simple closed-form expression is not easy to obtain. They provide an elegant way to define functions by breaking down a problem into simpler subproblems of the same form.

However, a few important things to keep in mind while writing a recursive function are:

1. Include base cases which have simple non-recursive solutions. These are essential to stop the recursion.
2. Ensure that the recursive calls are made on simpler instances of the same problem. This is necessary to guarantee that the recursive calls eventually reach the base cases.
3. The function must converge to a result in finite number of steps. This is necessary to avoid infinite recursive calls ( Stack overflow ).

[No external links included as instructed]