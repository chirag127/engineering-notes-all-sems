#### Operator in Core Java

- Operators in Java are symbols that are used to perform operations on variables and values  .
- Operators can be classified into different types based on the number of operands, the type of operation, and the precedence and associativity rules   .
- The types of operators in Java are:

  - Arithmetic operators: They are used to perform simple arithmetic operations on primitive data types, such as addition, subtraction, multiplication, division, modulus, and exponentiation    .
  - Unary operators: They are used to increment, decrement, or negate a value. They need only one operand. Examples are +, -, ++, --, and !   .
  - Assignment operator: It is used to assign a value to a variable. The symbol is =. It can also be combined with other operators to form compound assignment operators, such as +=, -=, *=, /=, %=, etc    .
  - Relational operators: They are used to compare two values and return a boolean result. Examples are ==, !=, >, <, >=, and <=    .
  - Logical operators: They are used to perform logical operations on boolean values, such as AND, OR, and NOT. Examples are &&, ||, and !    .
  - Bitwise operators: They are used to perform bit-level operations on integer values, such as AND, OR, XOR, NOT, and shift. Examples are &, |, ^, ~, <<, >>, and >>>    .
  - Conditional operator: It is a ternary operator that takes three operands and returns a value based on a condition. The symbol is ?:    .
  - instanceof operator: It is a binary operator that checks if an object is an instance of a class or an interface. The symbol is instanceof    .

- The precedence and associativity rules determine the order of evaluation of operators in an expression. Operators with higher precedence are evaluated before operators with lower precedence. Operators with the same precedence are evaluated according to their associativity, which can be either left-to-right or right-to-left   .
- The following table shows the precedence and associativity of operators in Java  :

| Operator type | Operators | Precedence | Associativity |
|---------------|-----------|------------|---------------|
| Postfix       | x++, x--  | Highest    | Left to right |
| Prefix        | ++x, --x, +x, -x, ~, ! | | Left to right |
| Multiplicative| *, /, %   | | Left to right |
| Additive      | +, -      | | Left to right |
| Shift         | <<, >>, >>> | | Left to right |
| Relational    | <, <=, >, >=, instanceof | | Left to right |
| Equality      | ==, !=    | | Left to right |
| Bitwise AND   | &         | | Left to right |
| Bitwise XOR   | ^         | | Left to right |
| Bitwise OR    | \|        | | Left to right |
| Logical AND   | &&        | | Left to right |
| Logical OR    | \|\|      | | Left to right |
| Conditional   | ?:        | | Right to left |
| Assignment    | =, +=, -=, *=, /=, %=, &=, ^=, \|=, <<=, >>=, >>>= | Lowest | Right to left |