### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results.
- In Python, functions are first class objects, which means they can be assigned to variables, passed as parameters, returned from other functions, and stored in data structures.
- Some examples of built-in higher order functions in Python are `map`, `filter`, `sorted`, and `reduce`.
- `map` applies a function to each element of an iterable and returns a new iterable with the results.
- `filter` returns a new iterable with only the elements that satisfy a predicate function.
- `sorted` returns a new sorted list from an iterable, optionally using a key function or a reverse flag.
- `reduce` applies a binary function to the elements of an iterable, from left to right, and returns a single value.
- Lambda expressions are anonymous functions that can be created using the `lambda` keyword. They can be used as arguments to higher order functions or assigned to variables.
- Lambda expressions have the syntax `lambda parameters: expression`, where parameters are optional and expression is a single statement that returns a value.
- Lambda expressions can access variables from the enclosing scope, but they cannot modify them.
- Lambda expressions are useful for creating simple functions that are only used once or for a short time.

Here is an example of using higher order functions and lambda expressions in Python:

```python
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to square each number and print the result
squared = map(lambda x: x**2, numbers)
print(list(squared)) # [1, 4, 9, 16, 25]

# Use filter to keep only the even numbers and print the result
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even)) # [2, 4]

# Use sorted to sort the numbers in descending order and print the result
descending = sorted(numbers, reverse=True)
print(descending) # [5, 4, 3, 2, 1]

# Use reduce to sum up the numbers and print the result
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total) # 15
```