### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

In Python, functions are considered first-class objects. This means that they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions. This allows for the creation of higher-order functions, which are functions that operate on other functions.

One example of a higher-order function is the `map()` function, which takes a function and an iterable as arguments and applies the function to each element of the iterable, returning a new iterable with the results.

Another example is the `filter()` function, which takes a function and an iterable as arguments and returns a new iterable containing only the elements of the original iterable for which the function returns `True`.

Lambda expressions, also known as anonymous functions, are a way to create small, one-time-use functions in Python. They are often used in conjunction with higher-order functions like `map()` and `filter()`. A lambda expression is defined using the `lambda` keyword, followed by a list of arguments, a colon, and an expression. The lambda expression returns the value of the expression when called with the given arguments.

For example, the following code uses a lambda expression to square each element of a list:

```python
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))
```

This code creates a lambda expression that takes one argument, `x`, and returns the value of `x` squared. This lambda expression is then passed as the first argument to the `map()` function, along with the list of numbers as the second argument. The `map()` function applies the lambda expression to each element of the list, returning a new iterable with the squared numbers. The `list()` function is then used to convert the iterable to a list, which is printed to the screen.

In summary, higher-order functions and lambda expressions are powerful tools in Python that allow for the creation of concise and flexible code. They are commonly used in functional programming and can help to make code more readable and reusable.