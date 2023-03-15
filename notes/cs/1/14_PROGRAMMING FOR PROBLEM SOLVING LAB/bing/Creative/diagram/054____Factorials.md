## Factorials

- A factorial is a mathematical operation that calculates the product of all positive integers from 1 to a given number.
- The factorial of a number n is denoted by n! and is defined as:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

- For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
- The factorial of 0 is defined as 1, i.e. 0! = 1
- The factorial function grows very fast as n increases. For example, 10! = 3628800 and 20! = 2432902008176640000
- The factorial function has many applications in mathematics, such as in combinatorics, probability, and calculus.
- One way to calculate the factorial of a number is to use a loop that multiplies the number by each smaller positive integer until 1 is reached. For example, in pseudocode:

function factorial(n)
  result = 1
  for i from n to 1
    result = result * i
  return result