# Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

## Higher Order Functions
- A higher order function is a function that either takes a function as an argument or returns a function as its result .
- Higher order functions allow us to create more abstract and modular code that can be reused and composed easily .
- Examples of higher order functions in Python are `map`, `filter`, `sorted`, `reduce`, `functools.partial`, `functools.lru_cache`, etc  .

## Functions as First Class Objects
- In Python, functions are first class objects, which means they have the following properties:
  - A function is an instance of the `Object` type.
  - You can store the function in a variable.
  - You can pass the function as a parameter to another function.
  - You can return the function from a function.
  - You can store them in data structures such as hash tables, lists, etc.

## Lambda Expressions
- A lambda expression is a way of creating anonymous functions in Python, which means they do not have a name .
- A lambda expression can take any number of arguments, but can only have one expression .
- The syntax of a lambda expression is `lambda arguments: expression` .
- A lambda expression can be used as an argument to a higher order function, or as a return value from a higher order function .
- Examples of lambda expressions are:

```python
# A lambda expression that adds two numbers
add = lambda x, y: x + y
print(add(3, 4)) # 7

# A lambda expression that filters out even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even) # [2, 4, 6]

# A lambda expression that returns a function that multiplies by a factor
def multiplier(factor):
  return lambda x: x * factor

double = multiplier(2)
print(double(5)) # 10
```