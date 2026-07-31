### Boolean Expression

- A Boolean expression is an expression that evaluates to produce a result which is a Boolean value.
- A Boolean value is either True or False, and the Python type is bool .
- A Boolean expression often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- Comparison operators are used to compare two values and return a Boolean value. They are: `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to)  .
- For example, the expression `1 <= 2` is True, while the expression `0 == 1` is False.
- Boolean expressions can also use logical operators to combine or modify Boolean values. They are: `and` (logical and), `or` (logical or), `not` (logical not)  .
- For example, the expression `True and False` is False, the expression `True or False` is True, and the expression `not True` is False.
- Logical operators follow the rules of Boolean algebra, which are:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T       | T      | F     |
| T | F | F       | T      | F     |
| F | T | F       | T      | T     |
| F | F | F       | F      | T     |

- Boolean expressions can also use parentheses to group terms and change the order of evaluation. For example, the expression `(True and False) or True` is True, while the expression `True and (False or True)` is also True.
- Boolean expressions are often used in conditional statements, such as `if`, `elif`, and `else`, to control the flow of the program based on some condition  .
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

- Boolean expressions can also be used in loops, such as `while` and `for`, to determine when to stop or continue the iteration  .
- For example, the following code snippet uses a Boolean expression to print the numbers from 1 to 10:

```python
number = 1
while number <= 10:
    print(number)
    number = number + 1
```

- Boolean expressions can also be used in functions, such as `any` and `all`, to check if any or all elements of an iterable (such as a list, tuple, or string) are truthy or falsy .
- A truthy value is a value that evaluates to True when converted to a Boolean, and a falsy value is a value that evaluates to False when converted to a Boolean .
- For example, the following code snippet uses the `any` function to check if any element of a list is positive:

```python
numbers = [0, -1, 2, -3, 4]
if any(number > 0 for number in numbers):
    print("There is at least one positive number in the list.")
else:
    print("There are no positive numbers in the list.")
```

- Boolean expressions can also be used in comprehensions, such as list comprehensions, to filter the elements of an iterable based on some condition .
- For example, the following code snippet uses a list comprehension to create a new list with only the even numbers from another list:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

- Boolean expressions are an essential part of Python programming, as they allow us to make decisions and perform actions based on some condition[^