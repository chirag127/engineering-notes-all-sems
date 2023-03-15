# Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- A comparison operator compares the values on either side of it and decides the relation among them.
- Some common comparison operators in Python are `==` (equal to), `!=` (not equal to), `<` (less than), `>` (greater than), `<=` (less than or equal to), and `>=` (greater than or equal to).
- A Boolean expression can also use logical operators, such as `and`, `or`, and `not`, to combine or negate other Boolean expressions.
- For example, the expression `price > 0 and quantity < 10` evaluates to true if both the conditions are true, false otherwise.
- The expression `price > 0 or quantity < 10` evaluates to true if at least one of the conditions is true, false otherwise.
- The expression `not price > 0` evaluates to true if the condition is false, false otherwise.
- A Boolean expression can also use parentheses to group subexpressions and change the order of evaluation.
- For example, the expression `(price > 0 and quantity < 10) or (price == 0 and quantity == 0)` evaluates to true if either of the subexpressions in parentheses is true, false otherwise.
- A Boolean expression can also use the `in` and `not in` operators to check if a value is or is not in a sequence, such as a string, a list, or a tuple.
- For example, the expression `'a' in 'apple'` evaluates to true, while the expression `'b' not in 'banana'` evaluates to false.
- A Boolean expression can also use the `is` and `is not` operators to check if two variables refer to the same object in memory.
- For example, the expression `a is b` evaluates to true if both `a` and `b` refer to the same object, false otherwise.
- A Boolean expression can also use the `isinstance()` function to check if an object is an instance of a certain class or type.
- For example, the expression `isinstance(1, int)` evaluates to true, while the expression `isinstance(1, str)` evaluates to false.