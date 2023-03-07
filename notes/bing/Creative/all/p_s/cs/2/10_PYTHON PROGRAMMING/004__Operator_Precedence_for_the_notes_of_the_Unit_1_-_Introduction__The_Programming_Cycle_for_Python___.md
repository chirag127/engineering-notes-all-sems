### Operator Precedence

- Operator precedence in Python means the order in which the Python interpreter executes operators. It tells the Python interpreter which operator should be evaluated first if a single statement contains more than one operator .
- Operator precedence is important to understand because it can affect the result of an expression. For example, the expression `10 + 20 * 30` is not the same as `(10 + 20) * 30` because of the different precedence of the `+` and `*` operators.
- Python follows the standard mathematical rules for operator precedence, which are summarized in the following table  :

| Operator | Description |
| :---: | :---: |
| `()` | Parentheses (grouping) |
| `**` | Exponentiation (raise to the power) |
| `+x`, `-x` | Positive, negative (unary plus, minus) |
| `~x` | Bitwise NOT |
| `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo |
| `+`, `-` | Addition, subtraction |
| `<<`, `>>` | Bitwise left shift, right shift |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `|` | Bitwise OR |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership, identity |
| `not x` | Logical NOT |
| `and` | Logical AND |
| `or` | Logical OR |
| `if – else` | Conditional expression |
| `:=` | Assignment expression |
| `lambda` | Lambda expression |

- The operators in the table are listed from highest to lowest precedence. This means that operators with higher precedence are evaluated before operators with lower precedence. For example, the expression `2 ** 3 * 4` is evaluated as `(2 ** 3) * 4` because `**` has higher precedence than `*`.
- If two operators have the same precedence, they are evaluated from left to right, except for the exponentiation operator `**`, which is evaluated from right to left. For example, the expression `2 ** 3 ** 2` is evaluated as `2 ** (3 ** 2)` because `**` is right-associative .
- Parentheses can be used to change the order of evaluation and override the operator precedence. Expressions inside parentheses are evaluated first, and then the result is used in the outer expression. For example, the expression `(10 + 20) * 30` is evaluated as `30 * 30` because the parentheses force the addition to be performed before the multiplication.

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of precedence of the arithmetic operators, you can use the acronym **PEMDAS**, which stands for **P**arentheses, **E**xponentiation, **M**ultiplication, **D**ivision, **A**ddition, **S**ubtraction.
- To remember the order of precedence of the bitwise operators, you can use the acronym **BESOR**, which stands for **B**itwise **E**xponentiation, **S**hift, **O**R, **R**emainder.
- To remember the order of precedence of the logical operators, you can use the acronym **NOA**, which stands for **N**OT, **A**ND, **O**R.
- To remember the order of precedence of the comparison operators, you can use the acronym **MINE**, which stands for **M**embership, **I**dentity, **N**on-equality, **E**quality.
- To remember the order of precedence of the assignment operators, you can use the acronym **LAC**, which stands for **L**ambda, **A**ssignment, **C**onditional.