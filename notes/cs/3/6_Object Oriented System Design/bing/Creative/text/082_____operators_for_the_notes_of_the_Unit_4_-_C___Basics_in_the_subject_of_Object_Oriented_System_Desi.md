### Operators

- Operators are symbols that perform some operations on one or more operands.
- Operands are the values or variables on which the operators act.
- Operators can be classified into different types based on the number of operands, the type of operation, and the precedence and associativity rules.
- The types of operators in C++ are:

  - Arithmetic operators: These operators perform basic mathematical operations such as addition, subtraction, multiplication, division, and modulus. They can be unary (one operand) or binary (two operands). For example, `+`, `-`, `*`, `/`, and `%`.
  - Relational operators: These operators compare two operands and return a boolean value (`true` or `false`) based on the result of the comparison. They are binary operators. For example, `==`, `!=`, `<`, `>`, `<=`, and `>=`.
  - Logical operators: These operators perform logical operations on one or more boolean operands and return a boolean value based on the result of the operation. They can be unary or binary operators. For example, `!` (logical NOT), `&&` (logical AND), and `||` (logical OR).
  - Bitwise operators: These operators perform bit-level operations on one or more integer operands and return an integer value based on the result of the operation. They are binary operators. For example, `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), and `>>` (right shift).
  - Assignment operators: These operators assign a value to a variable or modify the value of a variable based on some operation. They are binary operators. For example, `=` (simple assignment), `+=` (add and assign), `-=` (subtract and assign), `*=` (multiply and assign), `/=` (divide and assign), and `%=` (modulus and assign).
  - Increment and decrement operators: These operators increase or decrease the value of a variable by one. They can be unary or binary operators. They can also be prefix (before the operand) or postfix (after the operand) operators. For example, `++` (increment) and `--` (decrement).
  - Conditional operator: This operator evaluates a condition and returns one of two values based on whether the condition is true or false. It is a ternary operator (three operands). For example, `condition ? value1 : value2`.
  - Comma operator: This operator evaluates two expressions and returns the value of the second expression. It is a binary operator. For example, `expression1, expression2`.
  - Sizeof operator: This operator returns the size of a data type or a variable in bytes. It is a unary operator. For example, `sizeof(int)` or `sizeof(x)`.
  - Cast operator: This operator converts the type of an expression to another type. It is a unary operator. For example, `(int)x` or `(float)y`.
  - Pointer operators: These operators are used to access the address and the value of a pointer variable. They are unary operators. For example, `&` (address of) and `*` (value at address).
  - Member access operators: These operators are used to access the members (data or functions) of a class or a structure. They are binary operators. For example, `.` (member access) and `->` (pointer to member access).
  - Scope resolution operator: This operator is used to access the global variables or functions that have the same name as the local variables or functions. It is a binary operator. For example, `::x` or `::f()`.
  - New and delete operators: These operators are used to dynamically allocate and deallocate memory for objects. They are unary operators. For example, `new int` or `delete p`.