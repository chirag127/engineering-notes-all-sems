### Recursive definition of functions

- A recursive definition of a function defines values of the function for some inputs in terms of the values of the same function for other (usually smaller) inputs.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some initial or simplest inputs, such as 0 or 1.
- The recursive step specifies how to compute the value of the function for any input, given the values of the function for smaller inputs, using a relation or an operation.
- A recursive definition of a function is valid if it is well-defined, meaning that every input has a unique value, and it is computable, meaning that there is an algorithm or a procedure to calculate the value for any input.
- A recursive function is a function that calls itself as part of its definition.
- A recursive function must have a base case to terminate the recursion, and a recursive case to reduce the problem to a smaller subproblem.
- A recursive function can be converted to an equivalent iterative function using a stack or a loop.
- Recursive functions are useful for solving problems that have a recursive structure, such as factorial, Fibonacci, binary search, tree traversal, etc.

#### Example: Factorial function

- The factorial function n! is defined by the rules:
  - 0! = 1 (base case)
  - (n + 1)! = (n + 1)· n ! (recursive step)
- The factorial function can be implemented as a recursive function in Python as follows:

```python
def factorial(n):
  if n == 0: # base case
    return 1
  else: # recursive case
    return n * factorial(n - 1) # call itself with a smaller input
```

- The factorial function can also be implemented as an iterative function in Python as follows:

```python
def factorial(n):
  result = 1
  for i in range(1, n + 1): # loop from 1 to n
    result = result * i # update the result
  return result
```

- The factorial function can be visualized as a tree of recursive calls:

![factorial tree](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Recursion_tree_factorial_5.png/220px-Recursion_tree_factorial_5.png)