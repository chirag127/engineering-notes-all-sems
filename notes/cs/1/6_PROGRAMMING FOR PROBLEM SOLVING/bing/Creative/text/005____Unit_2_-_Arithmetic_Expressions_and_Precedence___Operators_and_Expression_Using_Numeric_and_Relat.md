## Unit 2 - Arithmetic Expressions and Precedence

- An **arithmetic expression** is a combination of operands and operators that can be evaluated to a single value of a certain type, such as int, float, or bool.
- Operands are the values or variables that are involved in the computation, such as 2, 3.14, x, or y.
- Operators are the symbols that specify the type of computation to be performed, such as +, -, *, /, %, **, etc.
- The **precedence** of an operator determines the order in which it is evaluated in an expression, relative to other operators. Operators with higher precedence are evaluated before operators with lower precedence, unless parentheses are used to override the order.
- The **associativity** of an operator determines the order in which it is evaluated in an expression, when there are multiple operators with the same precedence. Operators can be either left-associative or right-associative, meaning they are evaluated from left to right or from right to left, respectively.
- The following table summarizes the precedence and associativity of the arithmetic operators in Python, from highest to lowest:

| Operator | Description | Precedence | Associativity |
|----------|-------------|------------|---------------|
| ** | Exponentiation | Highest | Right |
| *, /, % | Multiplication, division, modulo | High | Left |
| +, - | Addition, subtraction | Low | Left |

- Some examples of arithmetic expressions and their evaluations are:

| Expression | Evaluation |
|------------|------------|
| 2 + 3 * 4 | 14 |
| (2 + 3) * 4 | 20 |
| 2 ** 3 ** 2 | 512 |
| 2 * 3 ** 2 | 18 |
| 5 / 2 | 2.5 |
| 5 // 2 | 2 |
| 5 % 2 | 1 |

- A **relational expression** is a combination of operands and operators that can be evaluated to a boolean value, either True or False, depending on the relationship between the operands. Relational operators are used to compare the values or variables, such as <, >, <=, >=, ==, !=, etc.
- Relational expressions can be used to test conditions, such as if statements, while loops, or logical expressions.
- The following table summarizes the precedence and associativity of the relational operators in Python, from highest to lowest:

| Operator | Description | Precedence | Associativity |
|----------|-------------|------------|---------------|
| ==, != | Equality, inequality | Highest | Left |
| <, <=, >, >= | Less than, less than or equal to, greater than, greater than or equal to | High | Left |

- Some examples of relational expressions and their evaluations are:

| Expression | Evaluation |
|------------|------------|
| 2 < 3 | True |
| 2 > 3 | False |
| 2 == 3 | False |
| 2 != 3 | True |
| 2 <= 3 | True |
| 2 >= 3 | False |

- A **mixed expression** is a combination of operands and operators that involve different types, such as int, float, or bool. In Python, mixed expressions are allowed, but the result type depends on the type conversion rules.
- **Type conversion** is the process of changing the type of a value or variable, either implicitly or explicitly. Implicit type conversion happens automatically when an operator or function requires a certain type of operand, such as +, -, *, /, etc. Explicit type conversion happens when the programmer uses a built-in function to change the type of a value or variable, such as int(), float(), bool(), str(), etc.
- The following table summarizes the type conversion rules for the arithmetic operators in Python:

| Operand 1 | Operand 2 | Operator | Result type |
|-----------|-----------|----------|-------------|
| int | int | +, -, *, //, % | int |
| int | int | / | float |
| int | int | ** | int or float, depending on the exponent |
| int | float | +, -, *, /, ** | float |
| int | float | //, % | float |
| float | float | +, -, *, /, ** | float |
| float | float | //, % | float |
| bool | bool | +, -, *, /, ** | int or float, depending on the operator |
| bool | bool | //, % | int |
| bool | int | +, -, *, /, ** | int or float, depending on the operator |
| bool | int | //