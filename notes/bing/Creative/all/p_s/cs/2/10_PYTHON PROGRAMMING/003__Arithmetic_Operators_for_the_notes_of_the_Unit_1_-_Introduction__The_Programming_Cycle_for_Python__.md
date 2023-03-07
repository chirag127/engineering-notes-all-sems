### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values in Python. They are binary operators, which means they operate on two operands. The following are the arithmetic operators in Python:

- `+` : Addition. It adds the values of the operands and returns the result. For example, `3 + 5` returns `8`.
- `-` : Subtraction. It subtracts the value of the right operand from the value of the left operand and returns the result. For example, `10 - 7` returns `3`.
- `*` : Multiplication. It multiplies the values of the operands and returns the result. For example, `4 * 6` returns `24`.
- `/` : Division. It divides the value of the left operand by the value of the right operand and returns the result as a floating-point number. For example, `15 / 3` returns `5.0`.
- `%` : Modulus. It returns the remainder of the division of the left operand by the right operand. For example, `17 % 5` returns `2`.
- `//` : Floor division. It returns the quotient of the division of the left operand by the right operand, rounded down to the nearest integer. For example, `9 // 2` returns `4`.
- `**` : Exponent. It raises the value of the left operand to the power of the right operand and returns the result. For example, `2 ** 3` returns `8`.

The following table shows some examples of arithmetic operators in Python:

| Expression | Result |
|------------|--------|
| `2 + 3`    | `5`    |
| `5 - 2`    | `3`    |
| `3 * 4`    | `12`   |
| `10 / 2`   | `5.0`  |
| `7 % 3`    | `1`    |
| `8 // 3`   | `2`    |
| `2 ** 4`   | `16`   |

Arithmetic operators have different precedence levels, which determine the order in which they are evaluated. The following is the order of precedence for arithmetic operators in Python, from highest to lowest:

- `**`
- `*`, `/`, `%`, `//`
- `+`, `-`

Parentheses can be used to change the order of evaluation. For example, `(2 + 3) * 4` returns `20`, while `2 + 3 * 4` returns `14`.

One possible mnemonic to remember the order of precedence for arithmetic operators is **PEMDAS**, which stands for **P**arentheses, **E**xponents, **M**ultiplication and **D**ivision, **A**ddition and **S**ubtraction. This is similar to the mnemonic **BODMAS** used in some countries, which stands for **B**rackets, **O**rders, **D**ivision and **M**ultiplication, **A**ddition and **S**ubtraction.

Another possible learning trick is to use the **left-to-right** rule, which means that operators with the same precedence level are evaluated from left to right. For example, in the expression `10 / 2 * 5`, the division and multiplication have the same precedence level, so the division is evaluated first, resulting in `5 * 5`, which is `25`. However, in the expression `10 / (2 * 5)`, the parentheses change the order of evaluation, so the multiplication is evaluated first, resulting in `10 / 10`, which is `1`.