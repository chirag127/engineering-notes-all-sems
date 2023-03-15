# Operators

Operators are symbols that perform some operations on one or more operands. Operands are the values or variables with which the operator works.

## Types of Operators

There are different types of operators in C++, such as:

- Arithmetic operators: These operators perform basic mathematical operations, such as addition, subtraction, multiplication, division, and modulo. For example, `+`, `-`, `*`, `/`, and `%`.
- Assignment operators: These operators assign a value to a variable. For example, `=`, `+=`, `-=`, `*=`, `/=`, and `%=`.
- Relational operators: These operators compare two operands and return a boolean value (true or false). For example, `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- Logical operators: These operators combine two or more boolean expressions and return a boolean value. For example, `&&` (logical AND), `||` (logical OR), and `!` (logical NOT).
- Bitwise operators: These operators perform operations on individual bits of an operand. For example, `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), and `>>` (right shift).
- Unary operators: These operators work on a single operand and change its value or state. For example, `++` (increment), `--` (decrement), and `-` (negation).
- Ternary operator: This operator takes three operands and returns a value based on a condition. For example, `condition ? value1 : value2`.
- Member access operators: These operators access the members (data or functions) of a class or structure. For example, `.` (dot operator) and `->` (arrow operator).
- Other operators: There are some other operators in C++, such as `sizeof` (returns the size of an operand), `new` (allocates memory for an object), `delete` (deallocates memory for an object), `[]` (array subscript), `()` (function call), and `,` (comma).

## Operator Precedence and Associativity

Operator precedence determines the order of evaluation of operators in an expression. Operators with higher precedence are evaluated before operators with lower precedence. For example, in the expression `a + b * c`, the multiplication operator (`*`) has higher precedence than the addition operator (`+`), so `b * c` is evaluated first and then added to `a`.

Operator associativity determines the order of evaluation of operators with the same precedence in an expression. Operators can be either left-associative or right-associative. Left-associative operators are evaluated from left to right, while right-associative operators are evaluated from right to left. For example, in the expression `a = b = c`, the assignment operator (`=`) is right-associative, so `b = c` is evaluated first and then assigned to `a`.

The following table shows the precedence and associativity of operators in C++ from highest to lowest:

| Operator | Description | Associativity |
| --- | --- | --- |
| `()` | Function call | Left to right |
| `[]` | Array subscript | Left to right |
| `.` | Member access | Left to right |
| `->` | Member access through pointer | Left to right |
| `++` `--` | Postfix increment and decrement | Left to right |
| `++` `--` | Prefix increment and decrement | Right to left |
| `+` `-` | Unary plus and minus | Right to left |
| `!` `~` | Logical NOT and bitwise NOT | Right to left |
| `(type)` | Type cast | Right to left |
| `*` | Dereference | Right to left |
| `&` | Address-of | Right to left |
| `sizeof` | Size-of | Right to left |
| `new` `delete` | Dynamic memory allocation and deallocation | Right to left |
| `*` `/` `%` | Multiplication, division, and modulo | Left to right |
| `+` `-` | Addition and subtraction | Left to right |
| `<<` `>>` | Bitwise left shift and right shift | Left to right |
| `<` `<=` `>` `>=` | Relational operators | Left to right |
| `==` `!=` | Equality and inequality operators | Left to right |
| `&` | Bitwise AND | Left