### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- In Python, functions are treated as **first class objects**, meaning that they can be assigned to variables, passed as arguments to other functions, returned from other functions, and stored in data structures such as lists, dictionaries, etc.
- A function that takes another function as an argument or returns another function as a result is called a **higher order function**. Higher order functions are useful for abstracting common patterns of computation, such as mapping, filtering, reducing, etc.
- Some examples of built-in higher order functions in Python are `map`, `filter`, `reduce`, `sorted`, etc. These functions can take a function and an iterable as arguments, and apply the function to each element of the iterable, returning a new iterable or a single value.
- A **lambda expression** is a way of creating anonymous functions in Python, i.e. functions that do not have a name. Lambda expressions can be used as arguments to higher order functions, or assigned to variables. The syntax of a lambda expression is `lambda parameters: expression`, where `parameters` are the names of the arguments, and `expression` is the body of the function. The expression can only be a single statement, and it must return a value.
- Lambda expressions are useful for creating simple functions that are only used once, or for defining functions inline. However, they are not equivalent to regular functions, as they have some limitations, such as not being able to use `return`, `break`, `continue`, or `raise` statements, or access global or nonlocal variables.
- Some examples of using lambda expressions are:

```python
# A lambda expression that adds two numbers
add = lambda x, y: x + y
print(add(3, 4)) # 7

# A lambda expression that returns the square of a number
square = lambda x: x ** 2
print(square(5)) # 25

# A lambda expression that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(6)) # True
print(is_even(7)) # False

# A lambda expression that reverses a string
reverse = lambda s: s[::-1]
print(reverse("hello")) # olleh

# Using lambda expressions as arguments to higher order functions
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums)) # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
sum = reduce(lambda x, y: x + y, nums) # 15
sorted_nums = sorted(nums, key=lambda x: -x) # [5, 4, 3, 2, 1]
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the syntax of a lambda expression, you can use the acronym LAMBDA: **L**ambda **A**rguments **M**ust **B**e **D**efined **A**fter colon.
- To remember the difference between regular functions and lambda expressions, you can use the word FUN: **F**unctions have a **U**nique **N**ame, lambda expressions do not.
- To remember the names and purposes of some common higher order functions, you can use the following associations:
  - `map`: maps a function to each element of an iterable, like a treasure map that shows where to apply the function.
  - `filter`: filters out the elements of an iterable that do not satisfy a function, like a coffee filter that separates the grounds from the liquid.
  - `reduce`: reduces an iterable to a single value by applying a function repeatedly, like a paper shredder that cuts documents into smaller pieces.
  - `sorted`: sorts an iterable according to a function, like a sorting machine that arranges items by some criteria.