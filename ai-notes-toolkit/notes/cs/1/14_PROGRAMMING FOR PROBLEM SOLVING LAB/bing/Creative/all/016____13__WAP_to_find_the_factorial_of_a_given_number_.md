## 13. WAP to find the factorial of a given number.

- A factorial of a positive integer n is the product of all positive integers from 1 to n, denoted by n!.
- For example, 5! = 1 x 2 x 3 x 4 x 5 = 120.
- The factorial of 0 is defined as 1, i.e., 0! = 1.
- To write a program to find the factorial of a given number, we can use a loop to iterate from 1 to n and multiply the result by each iteration.
- We can also use a recursive function to call itself with a smaller argument until it reaches the base case of 0 or 1.
- Here is an example of a program in Python that uses both methods to find the factorial of a given number:

```python
# Using a loop
def factorial_loop(n):
  # Initialize the result as 1
  result = 1
  # Loop from 1 to n
  for i in range(1, n + 1):
    # Multiply the result by i
    result = result * i
  # Return the result
  return result

# Using recursion
def factorial_recursion(n):
  # Base case: if n is 0 or 1, return 1
  if n == 0 or n == 1:
    return 1
  # Recursive case: return n times the factorial of n - 1
  else:
    return n * factorial_recursion(n - 1)

# Test the program
n = int(input("Enter a positive integer: "))
print("Factorial of", n, "using loop is:", factorial_loop(n))
print("Factorial of", n, "using recursion is:", factorial_recursion(n))
```