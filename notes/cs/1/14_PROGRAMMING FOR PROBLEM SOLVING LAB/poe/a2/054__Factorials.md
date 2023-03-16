 Here is the formal content on Factorials in Markdown format:

## Factorials

1. A factorial is the product of all positive integers less than or equal to a given positive integer n.
2. The factorial of n is denoted by n!. For example, 4! = 4 x 3 x 2 x 1 = 24.
3. The factorial function grows very quickly. For relatively small values of n, the factorial is:

- n = 0: 0! = 1
- n = 1: 1! = 1
- n = 2: 2! = 2
- n = 3: 3! = 6
- n = 4: 4! = 24
- n = 5: 5! = 120

4. The factorial function can be defined recursively as:

- 0! = 1
- n! = n x (n-1)! for n > 0

5. Factorials are commonly used to solve combinatorics problems in probability and statistics involving calculating permutations and combinations. For example, the number of permutations of n distinct objects is n!, and the number of combinations of n distinct objects taken k at a time is (n choose k) = n! / (k!(n-k)!).

6. The factorial function is not defined for negative integers and factorial of numbers greater than or equal to 13 will result in overflow for standard data types. Therefore, iterative algorithms are preferred over recursive algorithms to compute factorials of large numbers.