# Recursive Algorithms

Recursive algorithms are algorithms that solve a problem by calling themselves with smaller instances of the same problem. This approach is based on the principle of **divide and conquer**, where a problem is divided into smaller subproblems, which are then solved recursively until the base case is reached.

## Characteristics of Recursive Algorithms

- A recursive algorithm must have a **base case**, which is a condition that stops the recursion.
- A recursive algorithm must change its state and move towards the base case.
- A recursive algorithm must call itself, recursively.

## Advantages of Recursive Algorithms

- Recursive algorithms can be easier to understand and implement than their iterative counterparts.
- Recursive algorithms can be more elegant and concise than iterative algorithms.

## Disadvantages of Recursive Algorithms

- Recursive algorithms can be less efficient than iterative algorithms due to the overhead of function calls.
- Recursive algorithms can cause stack overflow if the recursion is too deep.

## Examples of Recursive Algorithms

- The factorial function can be implemented using a recursive algorithm.
- The Fibonacci sequence can be generated using a recursive algorithm.
- The binary search algorithm can be implemented using a recursive algorithm.

## Recurrence Relation & Generating Function

A recurrence relation is an equation that describes a sequence of values in terms of their previous values. A generating function is a mathematical tool used to encode a sequence of numbers as a single function. Generating functions can be used to solve recurrence relations by transforming the recurrence relation into an equation involving the generating function.

In the context of recursive algorithms, recurrence relations can be used to analyze the time complexity of the algorithm. The generating function can be used to find a closed-form solution for the recurrence relation, which can then be used to determine the time complexity of the algorithm.