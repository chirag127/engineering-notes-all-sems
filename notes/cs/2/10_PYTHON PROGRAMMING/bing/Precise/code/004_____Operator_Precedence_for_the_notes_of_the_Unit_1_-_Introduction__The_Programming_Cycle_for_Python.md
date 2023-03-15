### Operator Precedence

Operator precedence determines the order in which operations are performed when evaluating an expression. In Python, the order of precedence, from highest to lowest, is as follows:

1. Parentheses `()`
2. Exponentiation `**`
3. Unary negation `-x`
4. Multiplication `*`, division `/`, floor division `//`, and modulo `%`
5. Addition `+` and subtraction `-`
6. Bitwise left shift `<<` and bitwise right shift `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`
11. Identity `is`, `is not`
12. Membership `in`, `not in`
13. Logical NOT `not`
14. Logical AND `and`
15. Logical OR `or`

Operators with the same precedence are evaluated from left to right. Parentheses can be used to override the order of precedence and group operations in the desired order.

For example, in the expression `2 + 3 * 4`, the multiplication is performed before the addition, resulting in a value of `14`. However, if we want the addition to be performed first, we can use parentheses: `(2 + 3) * 4`, which results in a value of `20`.

It is important to understand the order of precedence when working with complex expressions to ensure that the operations are performed in the desired order.