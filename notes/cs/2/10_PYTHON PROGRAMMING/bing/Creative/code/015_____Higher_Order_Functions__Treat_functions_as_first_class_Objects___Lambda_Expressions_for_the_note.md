### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results .
- In Python, functions are first class objects, which means they can be assigned to variables, stored in data structures, passed as parameters, and returned as values .
- Some examples of built-in higher order functions in Python are `map`, `filter`, `sorted`, and `reduce`. These functions can take a function and an iterable as arguments and apply the function to each element of the iterable, returning a new iterable or a single value.
- Lambda expressions are anonymous functions that can be created using the `lambda` keyword . They can be used as arguments to higher order functions or assigned to variables. Lambda expressions have a simple syntax: `lambda parameters: expression`. They can only contain one expression and cannot have statements or annotations.
- Some advantages of using higher order functions and lambda expressions are:
  - They can make the code more concise, readable, and expressive .
  - They can avoid code duplication and improve modularity .
  - They can enable functional programming paradigms, such as map-reduce, currying, and partial application .
- Some disadvantages of using higher order functions and lambda expressions are:
  - They can make the code more difficult to debug and test .
  - They can introduce performance overhead and memory consumption .
  - They can reduce the readability and clarity of the code for some programmers .

: https://www.geeksforgeeks.org/higher-order-functions-in-python/
: https://www.codespeedy.com/higher-order-functions-in-python-map-filter-sorted-reduce/
: https://docs.python.org/3/library/functools.html