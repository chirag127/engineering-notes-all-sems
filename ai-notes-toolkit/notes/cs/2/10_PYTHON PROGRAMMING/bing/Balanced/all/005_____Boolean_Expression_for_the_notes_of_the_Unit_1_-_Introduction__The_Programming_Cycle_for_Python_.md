# Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- The comparison operators in Python are: `==` (equal to), `!=` (not equal to), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to).
- A Boolean expression can also use logical operators to combine multiple expressions into a more complex one. The logical operators in Python are: `and`, `or`, `not`.
- The `and` operator returns true if both operands are true, false otherwise.
- The `or` operator returns true if either operand is true, false otherwise.
- The `not` operator returns the opposite of the operand, true if it is false, false if it is true.
- A Boolean expression can also use parentheses to change the order of evaluation and make the expression more readable.
- For example, the expression `(price > 0) and (quantity > 0)` evaluates to true if both price and quantity are positive, false otherwise.
- The expression `not (price == 0) or (quantity == 0)` evaluates to true if either price is not zero or quantity is zero, false otherwise.
- The expression `(price > 0) and not (quantity == 0)` evaluates to true if price is positive and quantity is not zero, false otherwise.
- A Boolean expression can be used in conditional statements, such as `if`, `elif`, and `else`, to control the flow of the program based on the truth value of the expression.
- For example, the following code snippet prints a message based on the value of the variable `score`:

```python
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Pass")
else:
    print("Fail")
```

- A Boolean expression can also be used in loops, such as `while` and `for`, to determine when to stop or continue the iteration based on the truth value of the expression.
- For example, the following code snippet prints the numbers from 1 to 10 using a while loop:

```python
n = 1
while n <= 10:
    print(n)
    n = n + 1
```

- A Boolean expression can also be used in functions, such as `bool`, `any`, and `all`, to convert other types of values to Boolean values or to check if a sequence of values contains any or all true values.
- The `bool` function returns true if the argument has some sort of content, false otherwise. For example, `bool(0)` is false, `bool(1)` is true, `bool("")` is false, `bool("Hello")` is true, `bool(None)` is false, `bool([1, 2, 3])` is true, `bool([])` is false, etc.
- The `any` function returns true if any element of the iterable argument is true, false otherwise. For example, `any([True, False, False])` is true, `any([False, False, False])` is false, `any([0, 1, 2])` is true, `any([0, 0, 0])` is false, etc.
- The `all` function returns true if all elements of the iterable argument are true, false otherwise. For example, `all([True, True, True])` is true, `all([True, False, True])` is false, `all([1, 2, 3])` is true, `all([1, 0, 3])` is false, etc.