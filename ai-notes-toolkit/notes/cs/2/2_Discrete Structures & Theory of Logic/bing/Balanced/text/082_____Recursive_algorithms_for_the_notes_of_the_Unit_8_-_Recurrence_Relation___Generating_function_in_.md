### Recursive algorithms

- A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem.
- A recursive algorithm must have a base case, which is a condition that terminates the recursion when it is met.
- A recursive algorithm must also have a recursive case, which is a condition that reduces the problem size and invokes the algorithm again with the smaller problem.
- A recursive algorithm can be more concise, elegant, and intuitive than an iterative algorithm, but it may also be less efficient or more difficult to analyze.
- Examples of recursive algorithms are:
  - Factorial: To compute n!, we can use the following recursive formula: n! = n * (n-1)! if n > 1, and 1 if n = 1. The base case is n = 1, and the recursive case is n > 1.
  - Fibonacci: To compute the nth Fibonacci number, we can use the following recursive formula: F(n) = F(n-1) + F(n-2) if n > 2, and 1 if n = 1 or 2. The base case is n = 1 or 2, and the recursive case is n > 2.
  - Merge sort: To sort an array, we can use the following recursive algorithm: Divide the array into two halves, sort each half recursively, and merge the two sorted halves. The base case is when the array has one or zero elements, and the recursive case is when the array has more than one element.
  - Tower of Hanoi: To move n disks from one peg to another, we can use the following recursive algorithm: Move n-1 disks from the source peg to the auxiliary peg, move the largest disk from the source peg to the destination peg, and move n-1 disks from the auxiliary peg to the destination peg. The base case is when n = 1, and the recursive case is when n > 1.