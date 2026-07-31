### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results .
- In Python, functions are first class objects, which means they can be assigned to variables, stored in data structures, passed as parameters, and returned as values .
- Some examples of built-in higher order functions in Python are `map`, `filter`, `sorted`, and `reduce`. These functions can take a function and an iterable as arguments and apply the function to each element of the iterable, returning a new iterable or a single value.
- Lambda expressions are anonymous functions that can be created using the `lambda` keyword. They can be used as arguments to higher order functions or assigned to variables. Lambda expressions have a simple syntax: `lambda parameters: expression`. They can only contain one expression and cannot have statements or annotations.
- Decorators are a common use case of higher order functions in Python . They are functions that take another function as an argument and return a modified version of that function. Decorators can be used to add functionality, modify behavior, or check preconditions of a function. Decorators can be applied to a function using the `@` syntax or by calling the decorator function with the function as an argument.

: https://www.geeksforgeeks.org/higher-order-functions-in-python/
: https://www.codespeedy.com/higher-order-functions-in-python-map-filter-sorted-reduce/
: https://docs.python.org/3/library/functools.html
: https://stackoverflow.com/questions/62328661/what-is-the-difference-between-higher-order-functions-and-decorators