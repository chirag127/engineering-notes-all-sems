### Complexity of Algorithms

- Complexity of an algorithm is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is calculated asymptotically as n approaches infinity, to capture the behavior of the algorithm for large inputs.
- Complexity is about the algorithm itself, not the actual execution time or the hardware used.
- Complexity is expressed using the big O notation, which gives the upper bound of the number of operations executed by an algorithm as a function of n.
- For example, an algorithm that has a complexity of O(n) means that the number of operations grows linearly with the input size n.
- Complexity can be classified into two types: time complexity and space complexity.
- Time complexity is the amount of time required by the algorithm to solve the problem.
- Space complexity is the amount of memory required by the algorithm to solve the problem.
- Both time and space complexity depend on the choice of the algorithm, the input data, and the implementation details.
- Some common classes of complexity are:
  - Constant: O(1), the algorithm takes a constant amount of time or space regardless of the input size.
  - Logarithmic: O(log n), the algorithm takes a logarithmic amount of time or space with respect to the input size.
  - Linear: O(n), the algorithm takes a linear amount of time or space with respect to the input size.
  - Quadratic: O(n^2), the algorithm takes a quadratic amount of time or space with respect to the input size.
  - Cubic: O(n^3), the algorithm takes a cubic amount of time or space with respect to the input size.
  - Exponential: O(2^n), the algorithm takes an exponential amount of time or space with respect to the input size.
  - Factorial: O(n!), the algorithm takes a factorial amount of time or space with respect to the input size.
- The complexity of an algorithm can be analyzed by using the following steps:
  - Identify the basic operations that contribute to the running time or space usage of the algorithm, such as arithmetic operations, comparisons, assignments, etc.
  - Count the number of times each basic operation is executed as a function of the input size n.
  - Find the dominant term in the function, which has the highest growth rate as n increases.
  - Ignore the lower-order terms and the constant factors, and use the big O notation to express the complexity of the algorithm.
- For example, consider the following algorithm that computes the sum of the first n natural numbers:

```
Algorithm Sum(n)
  s = 0
  for i = 1 to n
    s = s + i
  return s
```

- The basic operations are the assignment s = 0, the comparison i <= n, the increment i = i + 1, the addition s = s + i, and the return s.
- The assignment s = 0 is executed once, so it contributes O(1) to the complexity.
- The comparison i <= n is executed n + 1 times, so it contributes O(n) to the complexity.
- The increment i = i + 1 is executed n times, so it contributes O(n) to the complexity.
- The addition s = s + i is executed n times, so it contributes O(n) to the complexity.
- The return s is executed once, so it contributes O(1) to the complexity.
- The total complexity of the algorithm is O(1) + O(n) + O(n) + O(n) + O(1) = O(3n + 2).
- The dominant term is 3n, which has the highest growth rate as n increases.
- The lower-order term 2 and the constant factor 3 can be ignored, and the complexity can be expressed as O(n) using the big O notation.
- Therefore, the complexity of the algorithm Sum(n) is O(n).