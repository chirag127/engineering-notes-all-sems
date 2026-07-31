### Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- The comparison operators in Python are: `==` (equal to), `!=` (not equal to), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to).
- A Boolean expression can also use logical operators to combine multiple comparison expressions, such as `and`, `or`, and `not`.
- The logical operators in Python follow these rules: `and` returns true if both operands are true, `or` returns true if either operand is true, `not` returns the opposite of the operand.
- A Boolean expression can also use parentheses to group subexpressions and change the order of evaluation.
- For example, the expression `(price > 0) and (quantity > 0)` evaluates to true if both price and quantity are positive numbers.
- A Boolean expression can also use the `in` and `not in` operators to check if a value is or is not in a sequence, such as a string, a list, or a tuple.
- For example, the expression `'a' in 'apple'` evaluates to true, while the expression `'b' not in 'banana'` evaluates to false.
- A Boolean expression can also use the `is` and `is not` operators to check if two variables refer to the same object in memory.
- For example, the expression `x is y` evaluates to true if x and y are the same object, while the expression `x is not y` evaluates to false if they are different objects.
- A Boolean expression can also use the `None` value to check if a variable has no value assigned to it.
- For example, the expression `x is None` evaluates to true if x has no value, while the expression `x is not None` evaluates to false if x has some value.
- A Boolean expression can also use any other value or variable as a truth value, following these rules: any non-zero number is true, any non-empty sequence is true, any other object is true, except for `None` and `False` .
- For example, the expression `bool(1)` evaluates to true, while the expression `bool(0)` evaluates to false .