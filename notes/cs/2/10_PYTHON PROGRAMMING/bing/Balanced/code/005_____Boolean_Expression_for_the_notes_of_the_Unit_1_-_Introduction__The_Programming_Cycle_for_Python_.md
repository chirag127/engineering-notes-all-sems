### Boolean Expression

- A Boolean expression is an expression that evaluates to produce a result which is a Boolean value.
- A Boolean value is one of the two values: `True` or `False`.
- The Python type for Boolean values is `bool`.
- A Boolean expression often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- Comparison operators are used to compare two values and return a Boolean value. They are: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- For example, the expression `1 <= 2` is `True`, while the expression `0 == 1` is `False`.
- Boolean expressions can also use logical operators to combine or modify Boolean values. They are: `and`, `or`, `not`.
- For example, the expression `True and False` is `False`, the expression `True or False` is `True`, and the expression `not True` is `False`.
- Boolean expressions can also use parentheses to group terms and change the order of evaluation. For example, the expression `(True and False) or True` is `True`, while the expression `True and (False or True)` is also `True`.
- Boolean expressions are often used in conditional statements, such as `if`, `elif`, and `else`, to control the flow of the program based on some condition.
- For example, the following code snippet uses a Boolean expression to check if a number is positive, negative, or zero:

```python
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

- Boolean expressions can also be used in loops, such as `while` and `for`, to determine when to stop or continue the iteration.
- For example, the following code snippet uses a Boolean expression to print the numbers from 1 to 10:

```python
number = 1
while number <= 10:
    print(number)
    number = number + 1
```

- Boolean expressions can also be used in functions, such as `bool`, `any`, and `all`, to convert or test other values for their truthiness.
- Truthiness is the concept that some values are considered `True` or `False` in a Boolean context, even if they are not of type `bool`.
- For example, the function `bool` returns `True` for any value that has some sort of content, such as a non-empty string, a non-zero number, or a non-empty sequence, and returns `False` for any value that is empty, zero, or `None` .
- For example, the expression `bool("Hello")` is `True`, while the expression `bool("")` is `False`.
- The function `any` returns `True` if any element in an iterable (such as a list, a tuple, or a set) is truthy, and returns `False` if all elements are falsy.
- For example, the expression `any([True, False, 0, 1])` is `True`, while the expression `any([False, 0, None, ""])` is `False`.
- The function `all` returns `True` if all elements in an iterable are truthy, and returns `False` if any element is falsy.
- For example, the expression `all([True, False, 0, 1])` is `False`, while the expression `all([True, 1, "Hello", [1, 2, 3]])` is `True`.

: Boolean Expressions in Python: Beginner to Expert
: Tutorial: Boolean Expressions in Python | CodeHS
: Python Booleans: Use Truth Values in Your Code – Real Python
: Python Booleans - W3Schools