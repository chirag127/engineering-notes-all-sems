# Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results.
- In Python, functions are first class objects, which means they can be assigned to variables, passed as parameters, returned from other functions, and stored in data structures.
- Some examples of built-in higher order functions in Python are map, filter, sorted, and reduce. They can be used to apply a function to a sequence of elements, filter out elements that satisfy a condition, sort elements based on a key function, and combine elements using a binary function.
- Lambda expressions are a way of creating anonymous functions in Python. They can be used as arguments to higher order functions or assigned to variables. They have the syntax: lambda parameters: expression
- Lambda expressions can only contain a single expression and cannot have statements, loops, or return statements. They are useful for creating simple functions that do not need a name or a docstring.
- Here are some examples of using higher order functions and lambda expressions in Python:

```python
# Define a function that squares a number
def square(x):
    return x**2

# Use map to apply the square function to a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared) # [1, 4, 9, 16, 25]

# Use lambda to create an anonymous function that doubles a number
doubled = list(map(lambda x: x*2, numbers))
print(doubled) # [2, 4, 6, 8, 10]

# Use filter to get only the even numbers from a list
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even) # [2, 4]

# Use sorted to sort a list of strings by their length
words = ["hello", "world", "python", "programming"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length) # ['world', 'hello', 'python', 'programming']

# Use reduce to get the product of all the numbers in a list
from functools import reduce
product = reduce(lambda x, y: x*y, numbers)
print(product) # 120
```