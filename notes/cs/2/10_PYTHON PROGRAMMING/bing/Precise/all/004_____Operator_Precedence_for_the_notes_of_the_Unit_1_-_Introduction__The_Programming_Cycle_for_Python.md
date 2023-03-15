### Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence.

In Python, the order of operator precedence, from highest to lowest, is as follows:

1. Parentheses `()`
2. Exponentiation `**`
3. Unary minus `-x`, unary plus `+x`, bitwise NOT `~x`
4. Multiplication `*`, division `/`, floor division `//`, modulo `%`
5. Addition `+`, subtraction `-`
6. Bitwise shift left `<<`, bitwise shift right `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison operators `==`, `!=`, `<`, `>`, `<=`, `>=`
11. Identity operators `is`, `is not`
12. Membership operators `in`, `not in`
13. Logical NOT `not`
14. Logical AND `and`
15. Logical OR `or`

When operators have the same precedence, they are evaluated from left to right. For example, in the expression `2 + 3 - 4`, the addition is performed first, followed by the subtraction.

Parentheses can be used to override the default order of operations. For example, in the expression `(2 + 3) * 4`, the addition is performed first, followed by the multiplication.

It is important to understand operator precedence when writing complex expressions in Python. Using parentheses to explicitly specify the order of operations can make the code more readable and prevent errors.