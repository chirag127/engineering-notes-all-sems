#### Operator in Core Java

- An operator is a symbol that performs a specific operation on one or more operands.
- An operand is a variable, constant, or expression on which the operator acts.
- For example, in the expression `a + b`, `+` is the operator and `a` and `b` are the operands.
- Operators are classified into different categories based on the number and type of operands they work on.
- The categories are:

  - Arithmetic operators: These operators perform basic mathematical operations such as addition, subtraction, multiplication, division, modulus, and exponentiation. For example, `a + b`, `a - b`, `a * b`, `a / b`, `a % b`, and `a ** b`.
  - Relational operators: These operators compare two operands and return a boolean value (true or false) based on the result of the comparison. For example, `a == b`, `a != b`, `a > b`, `a < b`, `a >= b`, and `a <= b`.
  - Logical operators: These operators perform logical operations on one or more boolean operands and return a boolean value based on the result of the operation. For example, `a && b`, `a || b`, and `!a`.
  - Bitwise operators: These operators perform bit-level operations on one or more integer operands and return an integer value based on the result of the operation. For example, `a & b`, `a | b`, `a ^ b`, `~a`, `a << b`, and `a >> b`.
  - Assignment operators: These operators assign a value to a variable or modify the value of a variable based on another value. For example, `a = b`, `a += b`, `a -= b`, `a *= b`, `a /= b`, `a %= b`, `a &= b`, `a |= b`, `a ^= b`, `a <<= b`, and `a >>= b`.
  - Unary operators: These operators act on a single operand and return a value based on the operand. For example, `+a`, `-a`, `++a`, `--a`, and `(type)a`.
  - Ternary operator: This operator acts on three operands and returns a value based on a condition. For example, `a ? b : c` returns `b` if `a` is true, otherwise returns `c`.
  - Special operators: These operators are used for special purposes such as accessing an object's property, invoking a method, creating an object, etc. For example, `a.b`, `a.b()`, `new A()`, `instanceof`, etc.

- The order of precedence and associativity of operators determine how an expression is evaluated in Java.
- The order of precedence is the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence.
- The associativity of operators is the direction in which operators are evaluated in an expression. Operators can be left-associative (evaluated from left to right) or right-associative (evaluated from right to left).
- The following table shows the order of precedence and associativity of operators in Java, from highest to lowest:

| Operator | Description | Associativity |
| --- | --- | --- |
| `()` | Parentheses | Left to right |
| `++` `--` | Postfix increment and decrement | Left to right |
| `++` `--` `+` `-` `!` `~` `(type)` | Prefix increment and decrement, unary plus and minus, logical NOT and bitwise complement, type cast | Right to left |
| `**` | Exponentiation | Right to left |
| `*` `/` `%` | Multiplication, division, and modulus | Left to right |
| `+` `-` | Addition and subtraction | Left to right |
| `<<` `>>` | Bitwise left and right shift | Left to right |
| `<` `<=` `>` `>=` | Relational less than, less than or equal to, greater than, greater than or equal to | Left to right |
| `==` `!=` | Relational equal to and not equal to | Left to right |
| `&` | Bitwise AND | Left to right |
| `^` | Bitwise XOR | Left to right |
| `|` | Bitwise OR | Left to right |
| `&&` | Logical AND | Left to right |
| `||` | Logical OR | Left to right |
| `?:` | Ternary conditional | Right to left |
| `=` `+=` `-=` `*=` `/