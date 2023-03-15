## Factorials

- A factorial is a mathematical operation that calculates the product of all positive integers from 1 to a given number n.
- The factorial of n is denoted by n! and is defined as:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

- For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
- The factorial of 0 is defined as 1, i.e. 0! = 1
- Factorials are used to count the number of ways to arrange or order a set of objects, such as permutations and combinations.
- Factorials grow very fast as n increases, so they are often approximated by using the Stirling's formula:

n! ≈ √(2πn) * (n/e)^n

- where e is the base of the natural logarithm, approximately equal to 2.71828
- Factorials can also be generalized to non-integer values by using the gamma function, which is defined as:

Γ(x) = ∫_0^∞ t^(x-1) * e^(-t) dt

- The gamma function satisfies the property that Γ(x+1) = x * Γ(x) for any positive x, and Γ(n+1) = n! for any positive integer n.