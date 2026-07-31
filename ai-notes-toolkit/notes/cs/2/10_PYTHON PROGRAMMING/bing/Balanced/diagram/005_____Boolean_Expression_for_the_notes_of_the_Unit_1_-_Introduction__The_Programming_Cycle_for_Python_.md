### Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- A comparison operator compares the values on either side of it and decides the relation among them. The most common comparison operators in Python are:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| == | Equal to | 5 == 3 | False |
| != | Not equal to | 5 != 3 | True |
| > | Greater than | 5 > 3 | True |
| < | Less than | 5 < 3 | False |
| >= | Greater than or equal to | 5 >= 3 | True |
| <= | Less than or equal to | 5 <= 3 | False |

- A Boolean expression can also use logical operators to combine two or more comparison expressions. The logical operators in Python are:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| and | True if both operands are true | 5 > 3 and 3 > 1 | True |
| or | True if either operand is true | 5 > 3 or 3 < 1 | True |
| not | True if the operand is false | not 5 > 3 | False |

- A Boolean expression can also use parentheses to group subexpressions and change the order of evaluation. For example, `(5 > 3) or (3 < 1)` is equivalent to `5 > 3 or 3 < 1`, but `(5 > 3 or 3) < 1` is not.
- A Boolean expression can also use the `in` and `not in` operators to check if a value is or is not in a sequence, such as a string, a list, or a tuple. For example, `'a' in 'apple'` is true, but `'b' in 'apple'` is false.
- A Boolean expression can also use the `is` and `is not` operators to check if two variables refer to the same object in memory. For example, `a = [1, 2, 3]` and `b = [1, 2, 3]` are two different lists, so `a is b` is false, but `a == b` is true.