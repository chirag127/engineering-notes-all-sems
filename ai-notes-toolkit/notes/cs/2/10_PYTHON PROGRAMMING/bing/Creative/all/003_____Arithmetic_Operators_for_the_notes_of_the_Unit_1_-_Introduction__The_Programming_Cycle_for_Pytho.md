# Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values. They can be applied to integers, floats, and complex numbers. The following are the common arithmetic operators in Python:

- `+` : Addition. It adds the operands and returns the sum. For example, `3 + 5` returns `8`.
- `-` : Subtraction. It subtracts the right operand from the left operand and returns the difference. For example, `10 - 7` returns `3`.
- `*` : Multiplication. It multiplies the operands and returns the product. For example, `4 * 6` returns `24`.
- `/` : Division. It divides the left operand by the right operand and returns the quotient. For example, `15 / 3` returns `5.0`. Note that the result is always a float, even if the operands are integers.
- `//` : Floor division. It divides the left operand by the right operand and returns the largest integer that is less than or equal to the quotient. For example, `17 // 4` returns `4`. Note that the result is always an integer, even if the operands are floats.
- `%` : Modulus. It returns the remainder of the division of the left operand by the right operand. For example, `9 % 4` returns `1`.
- `**` : Exponentiation. It raises the left operand to the power of the right operand and returns the result. For example, `2 ** 3` returns `8`.

Arithmetic operators follow the order of operations, which is:

- Parentheses `()`
- Exponentiation `**`
- Multiplication `*`, Division `/`, Floor division `//`, and Modulus `%`
- Addition `+` and Subtraction `-`

If the operands have different types, Python will try to convert them to a common type before performing the operation. This is called type conversion or type coercion. For example, if one operand is an integer and the other is a float, Python will convert the integer to a float and then perform the operation. For example, `3 + 4.5` returns `7.5`.

Some arithmetic operators can also be used with strings, lists, and tuples. For example, the `+` operator can be used to concatenate strings, lists, or tuples. The `*` operator can be used to repeat a string, list, or tuple a certain number of times. For example, `"Hello" + "World"` returns `"HelloWorld"`. `"Hi" * 3` returns `"HiHiHi"`. `[1, 2, 3] + [4, 5, 6]` returns `[1, 2, 3, 4, 5, 6]`. `[1, 2, 3] * 2` returns `[1, 2, 3, 1, 2, 3]`. `(1, 2, 3) + (4, 5, 6)` returns `(1, 2, 3, 4, 5, 6)`. `(1, 2, 3) * 2` returns `(1, 2, 3, 1, 2, 3)`. However, the `-`, `/`, `//`, `%`, and `**` operators cannot be used with strings, lists, or tuples. For example, `"Hello" - "World"` will raise a `TypeError`.

Arithmetic operators can be combined with the assignment operator `=` to create shorthand expressions. For example, `x += 1` is equivalent to `x = x + 1`. Similarly, `x -= 1` is equivalent to `x = x - 1`. The same applies to `*=`, `/=`, `//=`, `%=`, and `**=`. For example, `x *= 2` is equivalent to `x = x * 2`. These expressions are called augmented assignment operators. They can be used to update the value of a variable without repeating the variable name. For example, `x = 10` `x += 5` `print(x)` will print `15`.