### Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- The comparison operators in Python are:

| Operator | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| == | Equal to | 5 == 3 | False |
| != | Not equal to | 5 != 3 | True |
| > | Greater than | 5 > 3 | True |
| < | Less than | 5 < 3 | False |
| >= | Greater than or equal to | 5 >= 3 | True |
| <= | Less than or equal to | 5 <= 3 | False |

- A Boolean expression can also use logical operators to combine multiple comparison operators, such as `price > 0 and quantity < 10`.
- The logical operators in Python are:

| Operator | Meaning | Example | Result |
| -------- | ------- | ------- | ------ |
| and | True if both operands are true | True and False | False |
| or | True if at least one operand is true | True or False | True |
| not | True if the operand is false | not True | False |

- A Boolean expression can also use the `in` operator to check if a value is a member of a sequence, such as `x in [1, 2, 3]`.
- The `in` operator returns True if the value is found in the sequence, and False otherwise.
- A Boolean expression can also use the `is` operator to check if two variables refer to the same object, such as `x is y`.
- The `is` operator returns True if the variables have the same identity, and False otherwise.
- A Boolean expression can also use parentheses to change the order of evaluation, such as `(price > 0) or (quantity < 10)`.
- The parentheses determine which operators are evaluated first, following the rules of precedence.
- The order of precedence for the operators in Python is:

| Operator | Precedence |
| -------- | ---------- |
| () | Highest |
| not | High |
| in, is | Medium |
| <, <=, >, >=, !=, == | Low |
| and | Lower |
| or | Lowest |

- A Boolean expression can be used in conditional statements, such as `if`, `elif`, and `else`, to control the flow of the program based on the truth value of the expression.
- For example, the following code prints a message based on the value of `x`:

```python
x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

- A Boolean expression can also be used in loops, such as `while` and `for`, to determine when to stop or continue the iteration based on the truth value of the expression.
- For example, the following code prints the numbers from 1 to 10 using a while loop:

```python
n = 1
while n <= 10:
    print(n)
    n = n + 1
```

- A Boolean expression can also be used in functions, such as `return`, `break`, and `continue`, to return a value, exit a loop, or skip an iteration based on the truth value of the expression.
- For example, the following code defines a function that checks if a number is even using a Boolean expression:

```python
def is_even(n):
    return n % 2 == 0
```

- A Boolean expression can also be used in comprehensions, such as list, set, and dictionary comprehensions, to filter the elements based on the truth value of the expression.
- For example, the following code creates a list of even numbers from 1 to 10 using a list comprehension and a Boolean expression:

```python
even_numbers = [n for n in range(1, 11) if is_even(n)]
```

- A Boolean expression can also be used in built-in functions, such as `all`, `any`, and `filter`, to apply a condition to a sequence of values and return a Boolean value or a filtered sequence.
- For example, the following code uses the `all` function to check if all the elements in a list are positive using a Boolean expression:

```

One possible mnemonic to remember the order of precedence of the operators in Python is:

**P**lease **N**ot **I**n **C**lass **A**nd **O**utside

where each letter stands for the first letter of the operator:

**P**arentheses, **N**ot, **I**n, **C**omparison, **A**nd, **O**r

Another possible learning trick to remember the difference between the `is` and `==` operators is:

`is` checks **identity**, `==` checks **equality**

where identity means the same object, and equality means the same value.