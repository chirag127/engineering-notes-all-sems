### Recursive algorithms

- A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem.
- A recursive algorithm must have a base case, which is a condition that terminates the recursion when it is satisfied.
- A recursive algorithm must also have a recursive case, which is a condition that reduces the problem size and invokes the algorithm again with the smaller problem.
- A recursive algorithm can be more elegant and concise than an iterative algorithm, but it may also be less efficient or more difficult to understand.
- Examples of recursive algorithms are:
  - Merge sort, which sorts an array by recursively dividing it into two halves, sorting each half, and merging them together.
  - Quick sort, which sorts an array by recursively partitioning it around a pivot element, and sorting the left and right subarrays.
  - Tower of Hanoi, which moves a stack of disks from one peg to another, by recursively moving the top n-1 disks to a spare peg, moving the bottom disk to the destination peg, and moving the n-1 disks from the spare peg to the destination peg.
  - Fibonacci series, which generates the nth term of the sequence by recursively adding the previous two terms.
  - Factorial, which computes the product of all positive integers up to n by recursively multiplying n by the factorial of n-1.