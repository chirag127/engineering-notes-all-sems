## Factorials

- A factorial is a mathematical operation that calculates the product of all positive integers from 1 to a given number.
- The factorial of a number n is denoted by n! and is defined as:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

- For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
- The factorial of 0 is defined as 1, i.e. 0! = 1
- Factorials are used to count the number of ways to arrange or order a set of objects, such as permutations and combinations.
- Factorials grow very fast as the number increases. For example, 10! = 3,628,800 and 20! = 2,432,902,008,176,640,000
- The largest factorial that can be calculated using a standard 64-bit integer is 20!, as 21! would cause an overflow.
- Factorials can also be calculated using recursion, a technique where a function calls itself with a smaller argument until a base case is reached. For example, the recursive definition of n! is:

n! = n * (n-1)! if n > 0
n! = 1 if n = 0

- Factorials can also be extended to non-integer values using the gamma function, which is a special function that interpolates the factorial function. The gamma function is defined as:

Γ(x) = ∫<sub>0</sub><sup>∞</sup> t<sup>x-1</sup> e<sup>-t</sup> dt

- The gamma function satisfies the property that Γ(n+1) = n! for any positive integer n. For example, Γ(6) = 5! = 120
- The gamma function can also be evaluated for fractions, negative numbers, and complex numbers, but it is not defined for non-positive integers. For example, Γ(1/2) = √π and Γ(-1) is undefined.